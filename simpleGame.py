# Simple game in python

print('Hi, welcome to the Tim quiz!')
print('Try to get as many questions correct as possible...')

totalQuestions = 4
score = 0

ans = input('1. What is the name of my youtube channel? ')

if ans.lower() == 'tech with tim':
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('2. What is my age? ')

if ans == "17":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('3. What is my favourite sport? ')

if ans.lower() == "soccer":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('4. What is my favourite food? ')

if ans.lower() == "pizza":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


print("Thank you for playing, you got " + str(score) + ' questions correct!' )
percent = (score/totalQuestions) * 100
print("Mark: " + str(int(percent)) + '%')

if percent >= 50:
    print('Nice! You passed!')
else:
    print('Better luck next time')













    
