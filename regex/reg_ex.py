import re

pattern = re.compile(r"\d{3}-\d{3}-\d{4}")

# res = pattern.findall("Call me at 093-033-1500 or 066-482-3990!")

res = re.search(r"\d{3}-\d{3}-\d{4}","Call me at 093-033-1500")

print(res.group())