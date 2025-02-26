import re

# text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

# pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+", re.I)
# result = pattern.sub(r"\g<1> \g<2>", text)
# print(result)

def censor(input):
    censor_regex = re.compile(r"(\bfrack\w*\b)",re.IGNORECASE)
    pattern = censor_regex.sub(r"CENSORED", input)
    return pattern

censor("Frack you")                #"CENSORED you"
censor("I hope you fracking die")  #"I hope you CENSORED die"
censor("you fracking Frack")       #"You CENSORED CENSORED"