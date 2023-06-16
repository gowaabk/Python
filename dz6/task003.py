# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random
import task002 as t2

BOARD = 8
NUM_OF_SUCCSESS = 4

def random_queen_list(size):
    res = []
    i = 0
    while i < size:
        qeen = [random.randint(0,size), random.randint(0,size)]
        i += 1
    
        if qeen in res: i -= 1
        else:res.append(qeen)
    return res
        
def start_queens():
    count = 0
    count_tryes = 0
    while count < NUM_OF_SUCCSESS:
        count_tryes += 1
        t_qeen_list = random_queen_list(BOARD)
        if t2.queens(t_qeen_list):
            print(t_qeen_list, count_tryes)
            count += 1
            
start_queens()