import os
import subprocess

folders = [
    r"c:\Karetnikov_Lineage\public\images\heraldry\group01_stamps",
    r"c:\Karetnikov_Lineage\public\images\heraldry\group02_woodblocks",
    r"c:\Karetnikov_Lineage\public\images\heraldry\group03_coachmakers",
    r"c:\Karetnikov_Lineage\public\images\heraldry\group04_autographs_military",
    r"c:\Karetnikov_Lineage\public\images\heraldry\group05_kumanin",
    r"c:\Karetnikov_Lineage\public\images\heraldry\group06_zubkov_yukhin",
    r"c:\Karetnikov_Lineage\public\images\heraldry\group07_master_arms",
    r"c:\Karetnikov_Lineage\public\images\heraldry\logos_svg",
    r"c:\Karetnikov_Lineage\public\images\heraldry\logos_png"
]

for f in folders:
    os.makedirs(f, exist_ok=True)
    print(f"Created/verified: {f}")

# Download Kumanin Coat of Arms (OG XI, 54)
target_kumanin = r"c:\Karetnikov_Lineage\public\images\heraldry\group05_kumanin\01a_kumanin_og_11_54_original_archive.png"
url_kumanin = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Kumaniny_11-54.png"
cmd_kumanin = ["curl.exe", "-s", "-L", "-A", "KaretnikovLineageBot/1.0", url_kumanin, "-o", target_kumanin]
res1 = subprocess.run(cmd_kumanin)
print("Kumanin download:", res1.returncode, os.path.exists(target_kumanin), os.path.getsize(target_kumanin) if os.path.exists(target_kumanin) else 0)

# Download Vasily Petrovich Zubkov portrait
target_zubkov = r"c:\Karetnikov_Lineage\public\images\heraldry\group06_zubkov_yukhin\01_vasily_petrovich_zubkov_portrait.jpg"
url_zubkov = "https://upload.wikimedia.org/wikipedia/commons/8/8b/Zubkov_VP.jpg"
cmd_zubkov = ["curl.exe", "-s", "-L", "-A", "KaretnikovLineageBot/1.0", url_zubkov, "-o", target_zubkov]
res2 = subprocess.run(cmd_zubkov)
print("Zubkov download:", res2.returncode, os.path.exists(target_zubkov), os.path.getsize(target_zubkov) if os.path.exists(target_zubkov) else 0)
