# Задача 10 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2


import random


def GetHeadsOrTails(number: int):
    array = []
    for _ in range(0, number):
        randomNum = int(round(random.uniform(0, 1), 0))
        array.append(randomNum)
    return array

def GetMinNumsOfCoins(coins: list):
    numOfTails = 0
    numOfHeads = 0
    for i in range(len(coins)):
        if coins[i] == 0:
            numOfTails += 1
        else:
            numOfHeads += 1
    if numOfTails > numOfHeads:
        return numOfHeads
    else:
        return numOfTails

while True:
    try:
        coinsNumber = int(input('enter the number of coins: '))
        handfulOfCoins = GetHeadsOrTails(coinsNumber)
        print(handfulOfCoins)
        print(f'minimum number of coins to flip: {GetMinNumsOfCoins(handfulOfCoins)}')
        break
    except:
        print('Oops! That was no valid number. Try again...')



