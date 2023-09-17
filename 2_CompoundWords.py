words = ["ex", "exam", "mall", "am"]

def find_compound_words(words):
    compound_words = []
    word_set = set(words)
    for word in words:
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in word_set and suffix in word_set:
                compound_words.append(word)
                break
    return compound_words

print(find_compound_words(words))

