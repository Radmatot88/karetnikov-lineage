#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Patches dist/index.html so stylesheet links use relative './_heritage/' (compatible with both '/' and '/karetnikov-lineage/').
2. Deploys dist/ to GitHub Pages (https://radmatot88.github.io/karetnikov-lineage/) for 100% VPN-free access in Russia.
3. Deploys dist/ to Cloudflare Pages (https://karetnikov-family.pages.dev) via npx.cmd wrangler.
"""

import subprocess
import tempfile
import shutil
from pathlib import Path

PROJECT_ROOT = Path(r"c:\Karetnikov_Lineage")
DIST_DIR = PROJECT_ROOT / "dist"
REPO_NAME = "karetnikov-lineage"
GH_USER = "Radmatot88"


def run_cmd(cmd, cwd=None, check=True, shell=False):
    print(f"[EXEC] {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    res = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, encoding="utf-8", errors="replace", shell=shell)
    if res.stdout:
        print(res.stdout.strip())
    if res.stderr:
        print(res.stderr.strip())
    if check and res.returncode != 0:
        raise RuntimeError(f"Command failed ({res.returncode})")
    return res


def patch_relative_assets():
    idx = DIST_DIR / "index.html"
    txt = idx.read_text(encoding="utf-8")
    if 'href="/_heritage/' in txt:
        txt = txt.replace('href="/_heritage/', 'href="./_heritage/')
        idx.write_text(txt, encoding="utf-8")
        print("[OK] Patched dist/index.html stylesheet path to relative './_heritage/'")
    (DIST_DIR / ".nojekyll").write_text("", encoding="utf-8")


def deploy_github_pages():
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        for item in DIST_DIR.iterdir():
            dest = tmp_path / item.name
            if item.is_dir():
                shutil.copytree(item, dest)
            else:
                shutil.copy2(item, dest)

        run_cmd(["git", "init"], cwd=tmp_path)
        run_cmd(["git", "checkout", "-b", "gh-pages"], cwd=tmp_path)
        run_cmd(["git", "config", "user.name", GH_USER], cwd=tmp_path)
        run_cmd(["git", "config", "user.email", f"{GH_USER}@users.noreply.github.com"], cwd=tmp_path)
        run_cmd(["git", "add", "-A"], cwd=tmp_path)
        run_cmd(["git", "commit", "-m", "Deploy Native Mobile App & Relative Assets"], cwd=tmp_path)

        remote_url = f"https://github.com/{GH_USER}/{REPO_NAME}.git"
        run_cmd(["git", "remote", "add", "origin", remote_url], cwd=tmp_path)
        run_cmd(["git", "push", "--force", "origin", "gh-pages"], cwd=tmp_path)

    print(f"[OK] Deployed to GitHub Pages: https://radmatot88.github.io/{REPO_NAME}/")


def deploy_cloudflare_pages():
    print("[INFO] Updating Cloudflare Pages (karetnikov-family)...")
    run_cmd(
        "npx wrangler pages deploy dist --project-name karetnikov-family --branch main",
        cwd=PROJECT_ROOT,
        check=False,
        shell=True
    )


if __name__ == "__main__":
    patch_relative_assets()
    deploy_github_pages()
