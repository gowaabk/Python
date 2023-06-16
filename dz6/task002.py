# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# n = 2 # Количество ферзей на доске
# # x = [1,2] # Ферзи бьют друг друга
# # y = [1,2]
# # x = [1,2] # Ферзи не бьют друг друга
# # y = [1,5]
# x=[]
# y=[]
# def queens(x: list,y: list) -> bool:
#     # Ручной ввод координт ферзей
#     for i in range(n):
#         new_x, new_y = [int(s) for s in input("Введите координаты ферзя \n").split()]
#         print(new_x,new_y)
#         x.append(new_x)
#         y.append(new_y)

#     result = True
#     for i in range(n):
#         for j in range(i + 1, n):
#             if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
#                 result = False

#     return result


# print(queens(x,y))


def queens(qeen_list):
    flag = 0
    for qeen in qeen_list:

        for i in range(qeen[0] + 1 , len(qeen_list)):
            if [i, qeen[1]] in qeen_list: flag += 1
            
        for j in range(qeen[1] + 1, len(qeen_list)):
            if [qeen[0], j] in qeen_list: flag += 1

        i = 1
        j = 1
        while qeen[0] + i <= len(qeen_list) and qeen[1] - j <= 0:
            if [qeen[0] + i, qeen[1] - j] in qeen_list: flag += 1
            i += 1
            j += 1
        
        i = 1
        j = 1
        while qeen[0] + i <= len(qeen_list) and qeen[1] + j <= len(qeen_list):
            if [qeen[0] + i, qeen[1] + j] in qeen_list: flag += 1
            i += 1
            j += 1
        
    if flag == 0: 
        return True 
    else: return False

# data = [[1,1],[2,5]]
# print(queens(data))
