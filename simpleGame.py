# Simple game in python
import time

while True:#infinite loop
    print('Hi, welcome to the Tim quiz!')
    time.sleep(0.5)
    print('Try to get as many questions correct as possible...')
    time.sleep(0.5)

    totalQuestions = 4
    score = 0

    ans = input('1. What is the name of my youtube channel? ')
    if ans.lower() == 'tech with tim':
        time.sleep(0.5)
        print('Correct!')
        score += 1
    else:
        time.sleep(0.5)
        print('Incorrect')
        time.sleep(0.5)

    ans = input('2. What is my age? ')
    if ans == "17":
        time.sleep(0.5)
        print('Correct!')
        score += 1
    elif ans == "seventeen":
        time.sleep(0.5)
        print('Correct!')
        score += 1
    elif ans.lower() == "seventeen":
        time.sleep(0.5)
        print('Correct!')
        score += 1
    else:
        time.sleep(0.5)
        print('Incorrect')

    ans = input('3. What is my favourite sport? ')
    if ans.lower() == "soccer":
        time.sleep(0.5)
        print('Correct!')
        score += 1
    elif ans.lower() == "football":
        time.sleep(0.5)
        print('Correct!')
        score += 1
    else:
        time.sleep(0.5)
        print('Incorrect')


    ans = input('4. What is my favourite food? ')
    if ans.lower() == "pizza":
        time.sleep(0.5)
        print('Correct!')
        score += 1
    else:
        time.sleep(0.5)
        print('Incorrect')
        time.sleep(0.5)

    print("Calculating score!")
    time.sleep(0.5)
 

    print("Thank you for playing!")
    time.sleep(1)
    countdown=5
    for i in range(countdown):
        print(countdown)
        time.sleep(1)
        countdown -= 1

    percent = (score/totalQuestions) * 100
    print("Mark: " + str(int(percent)) + '%')
    if percent >= 50:
        print('Nice! You passed!')
    else:
        print('Better luck next time')
    
    print("If you want to quit, please press ctrl+c. If no, this game will run in an infinte loop")
    time.sleep(3)
