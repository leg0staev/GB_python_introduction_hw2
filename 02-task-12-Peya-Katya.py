# Задача 12 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

def LetsFindNums(sum, multiply: int):
    for x in range(1001):
        for y in range(1001):
            if x + y == sum and x * y == multiply:
                return x, y
            # else:
            #     return ("not exist", "not exist")


while True:
    try:
        S = int(input('enter the result of adding two numbers: '))
        P = int(input('enter the result multiplication of two numbers: '))
        nums = LetsFindNums(S, P)
        print(f'X -> {nums[0]}, Y -> {nums[1]}')
        break
    except:
        print('Oops! That was no valid numbers. Try again...')