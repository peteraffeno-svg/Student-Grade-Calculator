name=input('')
score=int(input(''))
print(f"Name:{name}")
print(f'Score:{score}')
if score>=70 and score  <=100:
    print('Grade:A')
elif score>=60 and score <=69:
    print('Grade:B')
elif score>=50 and score <=59:
    print('Grade:C')
elif score>=40 and score <=49:
    print('Grade:D')
else: 
    print('Grade:F')
if score>=50 and score  <=100:
    print('Result:Pass')
else: 
    print('Result:Fail')
add = 50
if score>=0 and score<=49:
    print(f'You need {add-score} to pass.')


