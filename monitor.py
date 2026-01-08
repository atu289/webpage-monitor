import os
import hashlib
import requests

URL = "https://www.ticketline.co.uk/venue/manchester-academy"
HASH_FILE = "hash.txt"

def get_hash():
    r = requests.get(URL, timeout=30)
    r.raise_for_status()
    return hashlib.md5(r.text.encode("utf-8")).hexdigest()

old_hash = None
if os.path.exists(HASH_FILE):
    with open(HASH_FILE, "r") as f:
        old_hash = f.read().strip()

new_hash = get_hash()

with open(HASH_FILE, "w") as f:
    f.write(new_hash)

changed = old_hash is not None and new_hash != old_hash

# GitHub Actions output
if "GITHUB_OUTPUT" in os.environ:
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"changed={str(changed).lower()}\n")
        f.write(f"url={URL}\n")
