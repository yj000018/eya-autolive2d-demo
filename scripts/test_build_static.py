"""Release boundary checks against the actual, unchanged demo sources."""
from pathlib import Path
import tempfile
import unittest
from build_static import ASSETS, ROOT, build


class ReleaseBoundary(unittest.TestCase):
    def test_exact_allowlist_and_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "release"
            proof = build(ROOT, output)
            self.assertEqual(len(proof["files"]), 8)
            self.assertEqual((output / "index.html").read_bytes(), (ROOT / "workflow_demo.html").read_bytes())
            self.assertEqual((output / "workflow_demo.html").read_bytes(), (ROOT / "workflow_demo.html").read_bytes())
            for name in ASSETS:
                self.assertEqual((output / "assets" / name).read_bytes(), (ROOT / "assets" / name).read_bytes())
            self.assertEqual({p.relative_to(output).as_posix() for p in output.rglob("*") if p.is_file()}, {row["path"] for row in proof["files"]})
            self.assertFalse(any(p.suffix == ".stretch" for p in output.rglob("*")))

    def test_deterministic_fresh_releases(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(build(ROOT, Path(directory) / "one"), build(ROOT, Path(directory) / "two"))

    def test_existing_release_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            marker = output / "existing"
            marker.write_bytes(b"preserve")
            with self.assertRaises(ValueError):
                build(ROOT, output)
            self.assertEqual(marker.read_bytes(), b"preserve")

    def test_symlink_source_is_rejected_before_output(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source"
            source.mkdir()
            (source / "workflow_demo.html").symlink_to(ROOT / "workflow_demo.html")
            output = Path(directory) / "release"
            with self.assertRaises(ValueError):
                build(source, output)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
