# def replace_digit(file):
#     with open(file,"r+",encoding="UTF-8") as f:
#         text = f.read()
#         # f.seek(0)
#         new_text = text
#         for d in text:
#             if d.isdigit():
#                 new_text = new_text.replace(d, '#')
#         f.seek(0)
#         f.write(new_text)

def replace_digit(file):
    with open(file,"r+",encoding="UTF-8") as f:
        text = f.read()
        new_text = ''.join('#' if digit.isdigit() else digit for digit in text)
        f.seek(0)
        f.write(new_text)

replace_digit("digits.txt")