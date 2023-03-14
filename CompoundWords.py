"""
TASK COMPOUND WORDS:
We have a list of words, each of which is a string of lowercase characters.
For example, such a list may contain words like "krat", "kratka", "owal" and "ka".
We assume that these strings are not too long.
Our task is to find the strings on this list that are compound words, i.e.
they consist of exactly two other strings occurring on the list.
On the previously presented example list, the only compound word is "kratka",
because it is a combination of the words "krat" and "ka".

"""

import time
start_time = time.time()

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

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
