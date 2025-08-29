# palindrome.py
text = input("Enter a word: ")

if text == text[::-1]:
    print(text, "is a Palindrome")
else:
    print(text, "is NOT a Palindrome")
3