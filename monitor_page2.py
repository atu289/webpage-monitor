import os
import hashlib
import requests

URL = "https://www.ticketline.co.uk/event/unavailable/13379205/sienna-spiro-manchester-academy-2026-05-16-19-00-00"
HASH_FILE = "hash_page2.txt"

def get_hash():
    r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
    r.raise_for_status()
    return hashlib.md5(r.text.encode("utf-8")).hexdigest()

old_hash = None
if os.path.exists(HASH_FILE):
    with open(HASH_FILE, "r", encoding="utf-8") as f:
        old_hash = f.read().strip()

new_hash = get_hash()

with open(HASH_FILE, "w", encoding="utf-8") as f:
    f.write(new_hash)

changed = old_hash is not None and new_hash != old_hash

if "GITHUB_OUTPUT" in os.environ:
    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
        f.write(f"changed={str(changed).lower()}\n")
        f.write(f"url={URL}\n")

print("OLD_HASH:", old_hash)
print("NEW_HASH:", new_hash)
print("CHANGED:", changed)
print("URL:", URL)
