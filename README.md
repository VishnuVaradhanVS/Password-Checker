# Password Strength Checker

A Python tool that evaluates the strength of passwords based on length, character variety, and common weak words. It also integrates with the HaveIBeenPwned API to check if the password has been exposed in known data breaches.

## Features
- Checks password strength (Weak, Medium, Strong)
- Validates length, uppercase, lowercase, digits, and special characters
- Detects common weak words
- Uses HaveIBeenPwned API to detect breached passwords
- Provides suggestions for improvement

## Requirements
- Python 3.x
- `requests` library

Install dependencies:
```bash
pip install requests
```
Usage
Run the script:

```bash
python password_checker.py
```
Enter a password when prompted. The tool will display:

Password strength rating

Suggestions for improvement

Whether it has been found in known breaches

Example Output
```
Enter a password to check: Password123!

Password Strength: Medium
Suggestions:
- Add special characters (@$!%*?&).
- Contains common word: 'password'

HaveIBeenPwned Check: Found in data breaches 1502 times.
```
