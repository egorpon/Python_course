'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

# def copy(file1,file2):
#     with open(file1, encoding="UTF-8") as f, open(file2, "w", encoding="UTF-8") as new_f:
#         text = f.read()
#         new_f.write(text)

def copy(file1,file2):
    with open(file1, encoding="UTF-8") as f: 
        text = f.read()
    with open(file2, "w", encoding="UTF-8") as new_f:
        new_f.write(text[::-1])
    

copy('story.txt', 'story_reversed.txt')