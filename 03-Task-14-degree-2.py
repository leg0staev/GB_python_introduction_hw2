# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
def DegreeOfTwo(limit: int):
    degrees = []
    degreeResult = 1
    while degreeResult <= limit:
        degrees.append(degreeResult)
        degreeResult *= 2
    return degrees


while True:
    try:
        userNum = int(input('enter a number, and I will output all the values of the exponent of two: '))
        degrees = DegreeOfTwo(userNum)
        print(f'X -> {degrees}')
        break
    except:
        print('Oops! That was no valid numbers. Try again...')