with open("dist/index.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
script_match = re.search(r'<script\b[^>]*>(.*?)</script>', html, re.DOTALL)
if script_match:
    js_code = script_match.group(1)
    with open("scratch/extracted_client_script.js", "w", encoding="utf-8") as out:
        out.write(js_code)
    print(f"Extracted JS code: {len(js_code)} chars")
