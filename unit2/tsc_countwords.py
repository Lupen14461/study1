
import re
words = {}
r = re.compile(r"[,!\*\.]")
with open("readme.md","r") as f:
    for line in f:
        for word in r.sub("",line.strip()).split(" "):
            if word in words:
                words[word] += 1
            words.setdefault(word,1)
print(words)