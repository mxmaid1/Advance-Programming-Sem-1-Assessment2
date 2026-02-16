import random

def randomInt(digits):
    if digits < 1:
        digits=1
    min_val = 10**(digits - 1)
    max_val = 10**digits - 1
    return random.randint(min_val, max_val)

def decideOperation():
    return "+-"[random.randint(0, 1)]

def displayProblem(Number1, Operation, Number2):
    while True:
        try:
            inputed = int(input(f"{Number1}{Operation}{Number2}="))
            return inputed
        except ValueError:
            print("Invalid input! Input a number.")

def isCorrect(inputed, rightanswer):
    print("Correct" if inputed == rightanswer else "Wrong, try again.")
    return inputed == rightanswer

def displayResults(score):
    print(f"Score: {score}/ 100")
    grades = [
        {"min": 90, "grade": "A+"},
        {"min": 80, "grade": "A"},
        {"min": 70, "grade": "B"},
        {"min": 60, "grade": "C"},
        {"min": 50, "grade": "D"},
        {"min": 0,  "grade": "F"}
    ]
    grade = "F" 
    for g in grades:
        if score >= g["min"]:
            grade = g["grade"]
            break 

    print("Grade:"+grade)
  
def displayMenu():
    print("Difficulty:")
    print("Option 1: Easy - 1 digit numbers")
    print("Option 2: Easy - 2 digit numbers")
    print("Option 3: Easy - 4 digit numbers")

    while True:
        try:
            level = int(input("Select Difficulty (Options 1-3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid Number, Valid Options (1, 2, or 3)")
        except ValueError:
            print("Error. Select Numbers 1-3")

def displayMenu():
    while True:
        score = 0
        level=1

        print("Difficulty:")
        print("Option 1: Easy - 1 digit numbers")
        print("Option 2: Medium - 2 digit numbers")
        print("Option 3: Hard - 4 digit numbers")

        while True:
            try:
                level = int(input("Select Difficulty (Options 1-3): "))
                if level in [1, 2, 3]:
                    break 
                else:
                    print("Invalid number. Valid options are 1, 2, or 3.")
            except ValueError:
                print("Error. Select numbers 1-3.")


        for i in range(1, 11): 
            if level==3:
                level=4

            num1 = randomInt(level)
            num2 = randomInt(level)
            operation = decideOperation()

            rightanswer = num1 + num2 if operation == "+" else num1 - num2

            print(f"Question {i}/10:")
            if isCorrect(displayProblem(num1,operation, num2), rightanswer):
                score += 10
            else:
                if isCorrect(displayProblem(num1,operation, num2), rightanswer):
                    score += 5

        displayResults(score)

        if input("Play again? (y/n): ") != "y":
            print("Game End")
            break

displayMenu()
