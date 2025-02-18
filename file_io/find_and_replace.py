'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file, wordtosearch, replacement):
    with open(file, "r+", encoding="UTF-8") as f:
        text = f.read()
        new_text = text.replace(wordtosearch, replacement)
        f.seek(0)
        f.write(new_text)
        f.truncate()



find_and_replace('story.txt', 'Alice', 'Colt') 