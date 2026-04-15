# Name: Prem Patel
# Description: Scan directory for potentially risky executable files

import os

SUSPICIOUS_EXTENSIONS = {
    ".dmg", ".pkg", ".app", ".command", ".sh",
    ".exe", ".bat", ".cmd", ".js", ".jar"
}

folder = input(
    "Enter a folder to scan (example: ~/(Folder Name)  or (/Users/(YOUR_USERNAME/FOLDER_NAME)):").strip()
folder = os.path.expanduser(folder)  # This Fixes (~)

if not os.path.isdir(folder):
    print("❌ That folder doesn't exist.")
    raise SystemExit

print("\n🔎 Scanning...\n")

count = 0
for root, dirs, files in os.walk(folder):
    for name in files:
        ext = os.path.splitext(name)[1].lower()
        if ext in SUSPICIOUS_EXTENSIONS:
            count += 1
            print(f"⚠️ Suspicious: {os.path.join(root, name)}")

print(f"\n✅ Done. Suspicious files found: {count}")
