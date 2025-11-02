"""Reorganize project structure"""
from pathlib import Path
import shutil

# Create directories
dirs = [
    "docs",
    "docs/guides",
    "tests"
]

for dir_path in dirs:
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    print(f"✓ Created {dir_path}/")

# Move documentation files
doc_files = {
    "README.md": "docs/README.md",
    "QUICKSTART.md": "docs/guides/QUICKSTART.md",
    "PRIVACY.md": "docs/guides/PRIVACY.md",
    "PROJECT_OVERVIEW.md": "docs/PROJECT_OVERVIEW.md",
    "GET_STARTED.txt": "docs/GET_STARTED.txt",
}

# Move test files
test_files = {
    "test_setup.py": "tests/test_setup.py",
    "test_chat.py": "tests/test_chat.py",
    "compare_models.py": "tests/compare_models.py",
}

print("\nMoving documentation files...")
for src, dst in doc_files.items():
    if Path(src).exists():
        shutil.move(src, dst)
        print(f"✓ Moved {src} → {dst}")

print("\nMoving test files...")
for src, dst in test_files.items():
    if Path(src).exists():
        shutil.move(src, dst)
        print(f"✓ Moved {src} → {dst}")

print("\n✅ Reorganization complete!")
