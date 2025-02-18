def replace_the_word(file,word = "fruit"):
    with open(file,"r+",encoding="UTF-8") as f:
        text = f.read()
        dct = {}
        for w in text.split(" "):
            dct[w] = text.count(w)
        
        f.seek(0)
        new_text = f.read()
        for w in dct:
            if dct[w]>1:
                new_text = new_text.replace(w,word)
        f.seek(0)
        f.write(new_text)
        f.truncate()

replace_the_word("fruits.txt")