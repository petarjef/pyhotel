from pathlib import Path
from PIL import Image

assets = Path(__file__).parent / "assets"
img = Image.open(assets / "icon.png").convert("RGBA")
img.save(assets / "icon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print("Napravljeno:", assets / "icon.ico")