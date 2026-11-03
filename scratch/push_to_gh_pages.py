import subprocess
import tempfile
import shutil
from pathlib import Path

PROJECT_ROOT = Path(r"c:\Karetnikov_Lineage")
DIST_DIR = PROJECT_ROOT / "dist"
REPO_NAME = "karetnikov-lineage"
GH_USER = "Radmatot88"

def deploy():
    print("[INFO] Patching relative assets for GitHub Pages mirror...")
    idx = DIST_DIR / "index.html"
    txt = idx.read_text(encoding="utf-8")
    if 'href="/_heritage/' in txt:
        txt = txt.replace('href="/_heritage/', 'href="./_heritage/')
        idx.write_text(txt, encoding="utf-8")
        print("[OK] Patched stylesheet path")
    (DIST_DIR / ".nojekyll").write_text("", encoding="utf-8")

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        print(f"[INFO] Copying {DIST_DIR} to {tmp_path}...")
        for item in DIST_DIR.iterdir():
            dest = tmp_path / item.name
            if item.is_dir():
                shutil.copytree(item, dest)
            else:
                shutil.copy2(item, dest)

        subprocess.run(["git", "init"], cwd=tmp_path, check=True)
        subprocess.run(["git", "checkout", "-b", "gh-pages"], cwd=tmp_path, check=True)
        subprocess.run(["git", "config", "user.name", GH_USER], cwd=tmp_path, check=True)
        subprocess.run(["git", "config", "user.email", f"{GH_USER}@users.noreply.github.com"], cwd=tmp_path, check=True)
        subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
        subprocess.run(["git", "commit", "-m", "Deploy V2: Light Imperial Vellum, Zero Emoji SVG, Senior A11y 60+"], cwd=tmp_path, check=True)

        remote_url = f"https://github.com/{GH_USER}/{REPO_NAME}.git"
        subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=tmp_path, check=True)
        print("[INFO] Pushing to GitHub Pages...")
        res = subprocess.run(["git", "push", "--force", "origin", "gh-pages"], cwd=tmp_path, capture_output=True, text=True)
        print(res.stdout)
        if res.returncode == 0:
            print(f"[SUCCESS] Deployed to GitHub Pages: https://radmatot88.github.io/{REPO_NAME}/")
        else:
            print(f"[ERROR] Git push failed:\n{res.stderr}")

if __name__ == "__main__":
    deploy()
