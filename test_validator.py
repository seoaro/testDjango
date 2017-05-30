import re

val = "010123412"
pattern = "^01[016789][1-9]\\d{6,7}$"
pattern = r"^01[016789][1-9]\d{6,7}$" # raw

if re.match(pattern, val):
    print("matched")
else:
    print("invalid")
