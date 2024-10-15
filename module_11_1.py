import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#   Библиотека Requests


response = requests.get('https://api.github.com')

print(response.status_code)
print()

# Создавать запросы посредством наиболее популярных HTTP-методов;
# Редактировать заголовки запросов и данных с помощью строки запроса, а также содержимого сообщения;
# Анализировать данные запросов и откликов; • создавать авторизированные запросы;
# Настраивать запросы с целью предотвращения сбоев и замедлений в работе приложения


# Библиотека matplotlib.pyplot


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')

x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

# Возможности библиотеки matplotlib
# Создание разных видов графиков
# Настройка внешнего вида графиков
# Интерактивная визуализация
# Интеграция выражений LaTeX
# Сохранение графиков


# Бибилотека Pandas

Data = [1, 3, 4, 5, 6, 2, 9]
s = pd.Series(Data)
Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
si = pd.Series(Data, Index)
print(si)
print("\n код pandas  \n")

# Возможности библиотеки Pandas

# Встроенные инструменты совмещения данных и обработки сопутствующих сведений
# Функция обмена электронными материалами между структурами памяти, а также различными файлами и документами
# Расширенные возможности при индексировании
# Слияние имеющихся информационных наборов
