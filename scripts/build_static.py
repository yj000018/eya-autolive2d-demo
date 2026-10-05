"""Package only the existing demo HTML and its six referenced images."""
from pathlib import Path
import argparse
import hashlib
import json
import re

ASSETS = (
    "eya_source.jpg", "seethrough_layers.jpg", "01_layers_loaded.webp",
    "04_joints_manual.webp", "05_rigging_complete.webp", "06_staging_mode.webp",
)
ROOT = Path(__file__).resolve().parents[1]


def build(source: Path, output: Path) -> dict:
    # No deletion or overwrite: a failed build leaves the existing release intact.
    if output.exists() or output.is_symlink():
        raise ValueError("Output already exists; use a new directory")
    payload = {"index.html": source / "workflow_demo.html", "workflow_demo.html": source / "workflow_demo.html"}
    payload.update({f"assets/{name}": source / "assets" / name for name in ASSETS})
    for path in payload.values():
        if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to(source.resolve()):
            raise ValueError("Required source is missing or escapes the source directory")
    html = payload["index.html"].read_text()
    if set(re.findall(r'src="([^"]+)"', html)) != {f"assets/{name}" for name in ASSETS}:
        raise ValueError("HTML image references differ from the reviewed six-asset allowlist")
    data = {name: path.read_bytes() for name, path in payload.items()}
    output.mkdir(parents=True)
    for name, content in data.items():
        destination = output / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
    return {"files": [{"path": name, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()} for name, content in sorted(data.items())], "source_html_unchanged": True, "image_files": 6, "provider_call": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output), indent=2))
