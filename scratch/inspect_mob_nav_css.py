with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
    text = f.read()

import re
for m in re.finditer(r'\.mob-nav-item[^{]*\{[^}]*\}', text):
    print(m.group(0))
    print('---')
