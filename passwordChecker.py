import re
import hashlib
import requests

COMMON_WORDS = ["password", "123456", "qwerty", "letmein", "admin"]

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Too short (minimum 8 characters).")
    else:
        strength += 1

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add digits.")

    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        feedback.append("Add special characters (@$!%*?&).")

    for word in COMMON_WORDS:
        if word in password.lower():
            feedback.append(f"Contains common word: '{word}'")
            strength -= 1
            break

    if strength <= 2:
        verdict = "Weak"
    elif strength <= 4:
        verdict = "Medium"
    else:
        verdict = "Strong"

    return verdict, feedback


def check_pwned(password):
    sha1_pwd = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1_pwd[:5], sha1_pwd[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        return False, "Error checking HIBP API."

    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return True, f"Found in data breaches {count} times."
    return False, "Not found in known breaches."


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")

    result, suggestions = check_password_strength(pwd)
    print("\nPassword Strength:", result)

    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print("-", s)

    pwned, msg = check_pwned(pwd)
    print("\nHaveIBeenPwned Check:", msg)
