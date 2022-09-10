#!/usr/bin/env python
# coding: utf-8

# # Home tasks
# Task #1
# Сумма цифр трехзначного числа
# Дано трехзначное число 179. Найдите сумму его цифр.
# Формат вывода
# Выведите ответ на задачу.
# Ответ
# Вывод программы:
# 17

# In[1]:


num1 = 1
num2 = 7
num3 = 9
print(num1 + num2 + num3)


# Task #2
# Электронные часы
# Дано число N. С начала суток прошло N минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент.
# Формат ввода
# Вводится число N — целое, положительное, не превышает 10⁷.
# Формат вывода
# Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
# Учтите, что число N может быть больше, чем количество минут в сутках.
# Примеры
# Тест 1
# Входные данные:
# 150
# Вывод программы:
# 2 30

# In[2]:


N = int(150)
N > 0
N <= 10 ** 7
h = (N // 60 % 24)
m = N % 60
print(h, m)


# In[ ]:




