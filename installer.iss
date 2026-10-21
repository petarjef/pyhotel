[Setup]
AppName=Python Hotel
AppVersion=1.1
DefaultDirName={localappdata}\PythonHotel
DefaultGroupName=Python Hotel
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
OutputDir=installer_output
OutputBaseFilename=PythonHotel_Setup
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
SetupIconFile=assets\icon.ico
UninstallDisplayIcon={app}\assets\icon.ico

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"

[Files]
Source: "release\app\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{autoprograms}\Python Hotel"; Filename: "{app}\.venv\Scripts\pythonw.exe"; Parameters: "main.py"; WorkingDir: "{app}"; IconFilename: "{app}\assets\icon.ico"
Name: "{autodesktop}\Python Hotel"; Filename: "{app}\.venv\Scripts\pythonw.exe"; Parameters: "main.py"; WorkingDir: "{app}"; IconFilename: "{app}\assets\icon.ico"; Tasks: desktopicon

[Run]
Filename: "{tmp}\python-installer.exe"; Parameters: "/quiet InstallAllUsers=0 PrependPath=1 Include_launcher=0 Include_test=0 Include_doc=0"; Check: NeedPython; StatusMsg: "Installing Python..."
Filename: "{code:PythonExe}"; Parameters: "-m venv ""{app}\.venv"""; Flags: runhidden; StatusMsg: "Creating Python enviornment..."
Filename: "{app}\.venv\Scripts\python.exe"; Parameters: "-m pip install --upgrade pip"; Flags: runhidden; StatusMsg: "Updating pip..."
Filename: "{app}\.venv\Scripts\python.exe"; Parameters: "-m pip install -r ""{app}\requirements.txt"""; Flags: runhidden; StatusMsg: "Downloading libaries (this may take couple of minutes)..."
Filename: "{app}\.venv\Scripts\pythonw.exe"; Parameters: "main.py"; WorkingDir: "{app}"; Description: "Launch Python Hotel"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

[Code]
var
  DownloadPage: TDownloadWizardPage;

function TryVersion(const V: String): String;
var
  P: String;
begin
  Result := '';
  if RegQueryStringValue(HKCU, 'Software\Python\PythonCore\' + V + '\InstallPath', 'ExecutablePath', P) and FileExists(P) then
    Result := P
  else if RegQueryStringValue(HKLM, 'Software\Python\PythonCore\' + V + '\InstallPath', 'ExecutablePath', P) and FileExists(P) then
    Result := P;
end;

function FindPython(): String;
begin
  Result := TryVersion('3.12');
  if Result = '' then Result := TryVersion('3.13');
  if Result = '' then Result := TryVersion('3.14');
end;

function PythonExe(Param: String): String;
begin
  Result := FindPython();
end;

function NeedPython(): Boolean;
begin
  Result := FindPython() = '';
end;

function OnDownloadProgress(const Url, FileName: String; const Progress, ProgressMax: Int64): Boolean;
begin
  Result := True;
end;

procedure InitializeWizard;
begin
  DownloadPage := CreateDownloadPage(SetupMessage(msgWizardPreparing), SetupMessage(msgPreparingDesc), @OnDownloadProgress);
end;

function NextButtonClick(CurPageID: Integer): Boolean;
begin
  Result := True;
  if (CurPageID = wpReady) and NeedPython() then
  begin
    DownloadPage.Clear;
    DownloadPage.Add('https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe', 'python-installer.exe', '');
    DownloadPage.Show;
    try
      try
        DownloadPage.Download;
      except
        SuppressibleMsgBox(AddPeriod(GetExceptionMessage), mbCriticalError, MB_OK, IDOK);
        Result := False;
      end;
    finally
      DownloadPage.Hide;
    end;
  end;
end;