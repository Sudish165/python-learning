import re

# --- First Pattern: Check if the input contains any lowercase letter (a-z) ---

# pattern = r'[a-z]'  # Pattern to find at least one lowercase letter
# string = input("Enter String: ")

# # re.search() will return a match object if the pattern is found
# if re.search(pattern, string):
#     print("Pattern found in the string")
# else:
#     print("Pattern not found in the string")

# --- Second Pattern: Check if the input is a valid email address format ---

# Regex Explanation:
# [A-Za-z]+    -> one or more letters (username part)
# \d+          -> one or more digits (optional numeric part in username)
# @+           -> one or more @ symbols (should ideally be just one, but kept for demonstration)
# [A-Za-z.]+   -> domain name (e.g., gmail, yahoo, etc.)
# .com         -> ends with .com

pattern = r'[A-Za-z0-9]+\d*@[A-Za-z.]+\.com'
string = input("Enter the email: ")

# Validate the email using re.search()
if re.search(pattern, string):
    print("Valid Email")
    print("Signed up successfully")
else:
    print("Invalid Email")
