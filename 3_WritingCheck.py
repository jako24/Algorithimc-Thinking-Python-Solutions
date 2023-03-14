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


