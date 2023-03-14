"""
TASK:
We have a problem where we are given two strings, with the first one being one character
longer than the second. Our task is to determine in how many ways we can remove one character
from the first string to obtain the second string. For example, there is only one way to
obtain the string 'barkowy' from the string 'barokowy', which is to remove the first
occurrence of the letter 'o'. On the other hand, the string 'abcdxxxef' can be transformed
into 'abcdxxef' in three ways, by removing any one of the 'x' letters.
"""

s1 = 'abcdxxxef'
s2 = 'abcdxxef'

def main():
    ways = writing_check(s1, s2)
    if ways == 0:
        print("The words are the same")
    elif ways == 1:
        print("There is one possible answer")
    else:
        print(f"There are {ways} ways to solve this problem")

def writing_check(invalid, valid):
    count = 0
    for i in range(len(invalid)):
        if invalid[:i] + invalid[i+1:] == valid:
            count += 1
    return count

if __name__ == "__main__":
    main()

# print(writing_check("barokowy", "barkowy"))

