"""Check and package this teaching Skill. Python standard library only.

This accepts only the JSON-quoted scalar subset used by this example's YAML
frontmatter. It is NOT a general YAML parser or WorkBuddy validation service.
It never calls a model, uploads a package, or installs a Skill.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import zipfile

HERE = Path(__file__).resolve().parent
REQUIRED = (
    "name", "display_name", "display_name_en", "description",
    "description_zh", "description_en", "version", "author",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "dist/meeting-action-checklist.zip")
    args = parser.parse_args()
    source = HERE / "meeting-action-checklist"
    text = (source / "SKILL.md").read_text(encoding="utf-8")
    pieces = text.split("---", 2)
    if len(pieces) != 3 or pieces[0] != "" or not pieces[1].startswith("\n"):
        raise ValueError("Expected YAML frontmatter bounded by ---")
    metadata = {}
    for line in pieces[1].strip().splitlines():
        key, separator, value = line.partition(":")
        if not separator or key in metadata:
            raise ValueError(f"Invalid or duplicate metadata field: {key}")
        metadata[key] = json.loads(value.strip())
    for key in REQUIRED:
        if not isinstance(metadata.get(key), str) or not metadata[key].strip():
            raise ValueError(f"Missing non-empty string field: {key}")
    if metadata["name"] != source.name:
        raise ValueError("Skill name must match this example's directory name")
    if not re.fullmatch(r"\d+\.\d+\.\d+", metadata["version"]):
        raise ValueError("Expected this example's x.y.z version format")
    files = sorted(
        (path for path in source.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(source.parent).as_posix(),
    )
    for path in files:
        if path.is_symlink() or not path.resolve().is_relative_to(source.resolve()):
            raise ValueError(f"Path outside package: {path}")
        if path.suffix != ".md":
            raise ValueError(f"This pure-text example must contain only .md files: {path}")
        body = path.read_text(encoding="utf-8")
        if not body.endswith("\n") or any(line != line.rstrip() for line in body.splitlines()):
            raise ValueError(f"Check final newline or trailing whitespace: {path}")
        for reference in re.findall(r"@(references/[A-Za-z0-9_./-]+\.md)", body):
            target = (source / reference).resolve()
            if not target.is_relative_to(source.resolve()) or not target.is_file():
                raise ValueError(f"Missing or unsafe local reference: {reference}")
    output = args.output.resolve()
    if output.is_relative_to(source.resolve()):
        raise ValueError("Write the generated ZIP outside the Skill source directory")
    output.parent.mkdir(parents=True, exist_ok=True)
    names = [path.relative_to(source.parent).as_posix() for path in files]
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for path, name in zip(files, names, strict=True):
            archive.write(path, name)
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None or archive.namelist() != names:
            raise ValueError("ZIP integrity check failed")
        for path, name in zip(files, names, strict=True):
            if archive.read(name) != path.read_bytes():
                raise ValueError(f"ZIP content mismatch: {name}")
    print(json.dumps({
        "status": "local_structure_and_zip_passed",
        "frontmatter_check": "restricted_json_quoted_scalars_not_general_yaml",
        "required_fields": list(REQUIRED),
        "files": names,
        "file_count": len(names),
        "output": str(output),
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "workbuddy_import_tested": False,
        "model_behavior_tested": False,
        "published": False,
        "warning": "Teaching author placeholder must be replaced before marketplace submission",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
