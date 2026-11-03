import subprocess
import os

PROJECT_ROOT = r"c:\Karetnikov_Lineage"
GH_USER = "Radmatot88"
REPO_NAME = "karetnikov-lineage"

def push_main():
    if not os.path.exists(os.path.join(PROJECT_ROOT, ".git")):
        print("[INFO] Initializing git in project root...")
        subprocess.run(["git", "init"], cwd=PROJECT_ROOT, check=True)
        subprocess.run(["git", "checkout", "-b", "main"], cwd=PROJECT_ROOT, check=True)
        subprocess.run(["git", "config", "user.name", GH_USER], cwd=PROJECT_ROOT, check=True)
        subprocess.run(["git", "config", "user.email", f"{GH_USER}@users.noreply.github.com"], cwd=PROJECT_ROOT, check=True)
        subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{GH_USER}/{REPO_NAME}.git"], cwd=PROJECT_ROOT, check=True)

    print("[INFO] Staging files...")
    subprocess.run(["git", "add", "."], cwd=PROJECT_ROOT, check=True)
    subprocess.run(["git", "commit", "-m", "V2 Architecture: Light Imperial Vellum, Zero Emoji SVG, Senior A11y 60+"], cwd=PROJECT_ROOT)
    print("[INFO] Pushing main branch to GitHub...")
    res = subprocess.run(["git", "push", "-u", "origin", "main"], cwd=PROJECT_ROOT, capture_output=True, text=True)
    print(res.stdout)
    if res.returncode == 0:
        print("[SUCCESS] Main branch pushed successfully!")
    else:
        print(f"[ERROR] {res.stderr}")

if __name__ == "__main__":
    push_main()
