#question 1 large numbers
def greater_than(a, b):
    answer = a ** 2
    return answer
print(greater_than(80, 2))
result = 6400
if result < 5000:
    print('False')
elif result > 5000:
    print('True')
else:
    print('No result')

#question 2 divisible by 10
def divisible_by_ten(num):
    calculation = num % 10
    return calculation
print(divisible_by_ten(200))
reminder = 0
if reminder == 0:
    print("true")
elif reminder > 0:
    print("false")
else:
    print("No result")
