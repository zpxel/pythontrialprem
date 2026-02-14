#!/usr/bin/python3
import hashlib, json, os, platform, datetime

CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
RED     = "\033[91m"
BOLD    = "\033[1m"
RESET   = "\033[0m"

CUSTOMER_FILE = ".customer_data.json"

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

# Same Activation Keys as Admin
activation_keys = [
    "ACT01abcd", "ACT02efgh", "ACT03ijkl", "ACT04mnop", "ACT05qrst",
    "ACT06uvwx", "ACT07yz12", "ACT083456", "ACT097890", "ACT10abcd",
    "ACT11efgh", "ACT12ijkl", "ACT13mnop", "ACT14qrst", "ACT15uvwx",
    "ACT16yz12", "ACT173456", "ACT187890", "ACT19abcd", "ACT20efgh",
    "ACT21ijkl", "ACT22mnop", "ACT23qrst", "ACT24uvwx", "ACT25yz12",
    "ACT263456", "ACT277890", "ACT28abcd", "ACT29efgh", "ACT30ijkl"
]

def hash_key(key):
    return hashlib.sha256(key.encode()).hexdigest()[:12]

def generate_activation():
    user_hash = int(hashlib.sha256(platform.node().encode()).hexdigest(), 16)
    index = user_hash % len(activation_keys)
    return activation_keys[index]

def save_local_data(act_key, key_type):
    hashed = hash_key(act_key + key_type)
    data = {
        "activation": act_key,
        "key_type": key_type,
        "hash": hashed,
        "timestamp": datetime.datetime.now().isoformat()
    }
    with open(CUSTOMER_FILE, "w") as f:
        json.dump(data, f, indent=4)
    return hashed

def main():
    banner()
    print(f"{CYAN}{BOLD}Customer Script - Activation & Premium Key{RESET}")
    print("="*50)

    mode = input("Choose Mode: [P]remium / [T]rial: ").strip().upper()

    if mode not in ["P", "T"]:
        print(f"{RED}[!] Invalid mode. Exiting.{RESET}")
        return

    key_type = "PREMIUM" if mode == "P" else "TRIAL"
    activation = generate_activation()
    hashed = save_local_data(activation, key_type)

    if key_type == "TRIAL":
        print(f"Your Trial Activation Key (hashed internally): {activation}")
        print("Trial valid for 90 days. Internal hash stored to prevent tampering.")
    else:
        print(f"Your Premium Activation Key: {activation}")
        print("Send this Activation Key to Admin to receive your Premium Key.")

    entered_key = input(f"Enter {key_type} Key provided by Admin: ").strip()

    if entered_key:
        if entered_key == hashed:
            print(f"{GREEN}[✓] {key_type} Key Accepted! Software Running...{RESET}")
        else:
            print(f"{RED}[!] Invalid {key_type} Key. Exiting.{RESET}")
    else:
        print(f"{YELLOW}[i] No {key_type} Key entered. Exiting.{RESET}")

if __name__ == "__main__":
    main()
