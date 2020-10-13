import re

sara = []

key = input("insert word  ")

with open('slov.txt') as file:
    wordLines = file.readlines()
    for words in wordLines:
        wordlist = re.split('\s+',words)

        for word in wordlist:

            result = re.match('\s*\w*'+key+'\s*\w*', word)
            if result is not None:

                sara.append(word)

print(sara)

