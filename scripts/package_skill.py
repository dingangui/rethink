"""Build the ZIP for Claude's custom skill uploader from the published skill."""

from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def build_archive() -> Path:
    root = Path(__file__).resolve().parents[1]
    skill = root / "skills" / "rethink"
    files = {
        "SKILL.md": skill / "SKILL.md",
        "agents/openai.yaml": skill / "agents" / "openai.yaml",
        "LICENSE": root / "LICENSE",
    }
    destination = root / "dist" / "rethink.zip"
    destination.parent.mkdir(exist_ok=True)
    with TemporaryDirectory(dir=destination.parent) as temporary:
        archive = Path(temporary) / destination.name
        with ZipFile(archive, "w") as bundle:
            for name, source in files.items():
                entry = ZipInfo(f"rethink/{name}")
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                bundle.writestr(entry, source.read_bytes(), compress_type=ZIP_DEFLATED)
        archive.replace(destination)
    return destination


if __name__ == "__main__":
    print(build_archive())
