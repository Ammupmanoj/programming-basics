# quiz.py
score = 0

print("Welcome to the Quiz! 🎓")

q1 = input("Q1: What is the capital of India? ")
if q1.lower() == "delhi":
    score += 1

q2 = input("Q2: What is 2 + 2? ")
if q2 == "4":
    score += 1

q3 = input("Q3: Who developed Python? ")
if q3.lower() == "guido van rossum":
    score += 1

print("Your score:", score, "/ 3")
