import re
def extract_phone(input):
    phone_regex = re.compile(r"\b\d{3}-\d{3}-\d{4}\b")
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None
# print(extract_phone("my number is 093-033-1500"))
# print(extract_phone("my number is 093-033-150012312"))
# print(extract_phone("093-033-1500 adasdsa"))
# print(extract_phone("093-033-1500"))
    
def extract_all_phones(input):
    phone_regex = re.compile(r"\b\d{3}-\d{3}-\d{4}\b")
    match = phone_regex.findall(input)
    return match

# print(extract_all_phones("my number is 093-033-1500 or call me at 066-583-0654"))
# print(extract_all_phones("my number is 093-033-15"))



# def is_valid_phone(input):
#     phone_regex = re.compile(r"^\d{3}-\d{3}-\d{4}$")
#     match = phone_regex.search(input)
#     if match:
#         return True
#     return False


def is_valid_phone(input):
    phone_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False


print(is_valid_phone("093-033-1500"))
print(is_valid_phone("093-033-1500 adsa"))
print(is_valid_phone("dsadasd 093-033-1500 adsa"))
print(is_valid_phone("093-033-15"))