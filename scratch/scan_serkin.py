import os
from pathlib import Path

SKIP_DIRS = {"node_modules", ".git", ".astro", "dist", "venv", ".venv", "__pycache__", ".pnpm"}

def scan_dir(root_path: str):
    p = Path(root_path)
    if not p.exists():
        print(f"Directory not found: {root_path}")
        return
    print(f"\n==================== {root_path} ====================")
    for root, dirs, files in os.walk(p):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel_root = os.path.relpath(root, p)
        for f in sorted(files):
            fp = Path(root) / f
            try:
                size = fp.stat().st_size
            except Exception:
                size = 0
            print(f"  {rel_root}\\{f}  ({size:,} bytes)")

if __name__ == "__main__":
    scan_dir(r"C:\Серкин, Циолковский")
    scan_dir(r"C:\Родословная_ИИ")
    scan_dir(r"C:\Prime_Lead_Bussiness\Prime_Lead_Labs")
