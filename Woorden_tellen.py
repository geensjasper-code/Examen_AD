def woorden_splitsen(file):
    with open(file, "r") as f:                # automatically closes the file
        text = f.read()                       # optional: make lowercase
        for char in ".?!,;":                  # loop over punctuation once
            text = text.replace(char, "")
        return text.split()

def woorden_tellen(file):
    wordcount = {}
    with open(file, "r") as f:  # Open the file in read mode and automatically close it when done
        text = f.read().lower()
        for char in ".?!,;":
            text = text.replace(char, "")
        words = text.split()
        for word in words:
            if word in wordcount:  # if word already exists, increment count
                wordcount[word] += 1
            else:  # if word is new, set count to 1
                wordcount[word] = 1
        return wordcount
