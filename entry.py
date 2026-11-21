"""Ship one finished 1024x1024 PNG: the passport spread rendered offline from
design/page.html into design/entry.png. The program only copies those bytes, so a
run is deterministic and needs no browser and no network."""

import os
from pathlib import Path

png = Path(__file__).with_name("design") / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
data = png.read_bytes()
if len(data) > 1_048_576:
    raise SystemExit(f"entry too large: {len(data)}")
(out_dir / "entry.png").write_bytes(data)
print(f"wrote {out_dir / 'entry.png'} ({len(data)} bytes)")
