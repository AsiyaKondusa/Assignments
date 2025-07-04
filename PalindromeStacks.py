def is_palindrome(word):
    stack = []

    for char in word:
        stack.append(char)

    for char in word:
        if char != stack.pop():
            return False
        return True

s = input("Enter a word: ")

if is_palindrome(s):
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")