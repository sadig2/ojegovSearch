print("before if")

if __name__ == "__main__":
    from voc import searchWord
    word = input("insert name  ")

    searchWord(word)
    print(__name__)