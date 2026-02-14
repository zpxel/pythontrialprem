#!/usr/bin/python3
import hashlib, json, os

CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
RED     = "\033[91m"
BOLD    = "\033[1m"
RESET   = "\033[0m"

ADMIN_FILE = "admin_activation.json"

# ====================== BANNER ======================
def banner():
    print(f"""
{CYAN}---------------------------------{RESET}
{GREEN}Author  : {YELLOW}zpxel{RESET}
{GREEN}Note    : {YELLOW}Buy me a coffee ☕ 0945-156-2126{RESET}
{GREEN}Info    : {YELLOW}Free to use{RESET}
{CYAN}---------------------------------{RESET}
""")
# ====================================================

# Fixed Activation Keys
activation_keys = [
    "ACT01abcd", "ACT02efgh", "ACT03ijkl", "ACT04mnop", "ACT05qrst",
    "ACT06uvwx", "ACT07yz12", "ACT083456", "ACT097890", "ACT10abcd",
    "ACT11efgh", "ACT12ijkl", "ACT13mnop", "ACT14qrst", "ACT15uvwx",
    "ACT16yz12", "ACT173456", "ACT187890", "ACT19abcd", "ACT20efgh",
    "ACT21ijkl", "ACT22mnop", "ACT23qrst", "ACT24uvwx", "ACT25yz12",
    "ACT263456", "ACT277890", "ACT28abcd", "ACT29efgh", "ACT30ijkl"
]

# Generate keys (Premium & Trial)
def generate_premium_key(act_key):
    return hashlib.sha256((act_key + "PREMIUM").encode()).hexdigest()[:12]

def generate_trial_key(act_key):
    return hashlib.sha256((act_key + "TRIAL").encode()).hexdigest()[:12]

def generate_keys():
    mapping = {act: {"premium_key": generate_premium_key(act),
                     "trial_key": generate_trial_key(act)} for act in activation_keys}
    with open(ADMIN_FILE, "w") as f:
        json.dump(mapping, f, indent=4)
    print(f"{GREEN}[✓]{RESET} Generated {len(activation_keys)} Activation → Premium/Trial keys.")
    print(f"{YELLOW}[i]{RESET} Saved to {ADMIN_FILE}")

def lookup_key():
    if not os.path.exists(ADMIN_FILE):
        print(f"{RED}[!] Admin JSON missing! Generate keys first.{RESET}")
        return
    with open(ADMIN_FILE, "r") as f:
        mapping = json.load(f)
    act = input("Enter Activation Key to lookup Premium/Trial Key: ").strip()
    if act in mapping:
        print(f"{GREEN}[✓] Activation Key Found!{RESET}")
        print(f"Premium Key: {mapping[act]['premium_key']}")
        print(f"Trial Key  : {mapping[act]['trial_key']}")
    else:
        print(f"{RED}[!] Activation Key not found!{RESET}")

def main():
    banner()
    print(f"{CYAN}{BOLD}Admin Tool - Generate & Lookup Keys{RESET}")
    print("="*40)
    choice = input("Choose action: [G]enerate / [L]ookup: ").strip().upper()
    if choice == "G":
        generate_keys()
    elif choice == "L":
        lookup_key()
    else:
        print(f"{RED}[!] Invalid option.{RESET}")

if __name__ == "__main__":
    main()
