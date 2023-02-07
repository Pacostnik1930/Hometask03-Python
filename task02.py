# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

print('Количество элементов в массиве:')
n = int(input())
list = []
for i in range(1,n + 1):
     list.append(i)
print(list)
print('Введите число Х:')
x = int(input())
for i in range (len(list)):
     if list[i] < n:
          find_num =- 1
else: 
     find_num =+ 0
     if list[i] >= n and list[i] - n <= find_num - n:
        find_num = list[i]
     elif list[i] <= n and find_num - n <= list[i] - n:
        find_num = list[i]
     print(find_num ,':','Самый близкий по значению элемент') 