"""Rebuild the installable stylesheet while retaining its embedded font."""
from pathlib import Path

root = Path(__file__).resolve().parent
target = root / "theme.css"
marker = "/* Claude Warm."
current = target.read_text()
if marker not in current:
    raise SystemExit("The existing theme.css must contain the embedded font and theme marker.")
stylesheet = current.split(marker, 1)[0] + (root / "treatments.css").read_text()
if len(stylesheet.encode()) > 256 * 1024:
    raise SystemExit("The stylesheet exceeds BB's size limit.")
target.write_text(stylesheet)
print(f"Built {target.name}: {len(stylesheet.encode())} bytes")
