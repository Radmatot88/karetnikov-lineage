import urllib.request

try:
    resp = urllib.request.urlopen("http://localhost:4321", timeout=3)
    print("Port 4321 responded:", resp.status)
except Exception as e:
    print("Port 4321 error:", e)
