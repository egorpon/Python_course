import re


# url_regex = re.compile(r"(https?)://((www\.)?[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)")
# match = url_regex.search("https://www.dasd.ua/dasd")
# print(f"Protocol: {match.group(1)}")
# print(f"Domain: {match.group(2)}")
# print(f"Everything else: {match.group(4)}")


# def parse_bytes(input):
#     bytes_regex = re.compile(r"\b[10]{8}\b")
#     match = bytes_regex.findall(input)
#     print(match)


# give a name
# def parse_name(input):
#     name_regex = re.compile(r"^(Mr\.|Mrs\.|Ms\.|Mdme\.|) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$")
#     match = name_regex.search(input)
#     print(match.group())
#     print(match.group('first'))
#     print(match.group('last'))

# parse_name("Mrs. Tilda Swinton")


def parse_date(input):
    date_regex=re.compile(r"^\b(?P<d>[0-9]{2})[/,.](?P<m>[0-9]{2})[/,.](?P<y>[0-9]{4})\b$")
    matches = date_regex.search(input)
    if matches:
        return{"d":matches.group("d"),
               "m":matches.group("m"),
               "y": matches.group("y")}
    return None

# {'d': '01', 'm': '22', 'y': '1999'} is not None : expected parse_date(it is 01/22/1999') to return None


print(parse_date("01/22/1999")) # {'d': '01', 'm': '22', 'y': '1999'}
print(parse_date("12,04,2003"))  #{'d': '12', 'm': '04', 'y': '2003'}
print(parse_date("12.11.2003"))  #{'d': '12', 'm': '11', 'y': '2003'}
print(parse_date("12.11.200312")) #None