# Task№3
import requests
import re

# Получаем HTML-код страницы
response = requests.get('https://www.python.org')
html_text = response.text

# Используем regex для поиска всех символов
all_chars = re.findall(r'.', html_text)

# Считает количество вхождений каждого символа
char_counts = {}
for char in all_chars:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

# Отсортировываем символы по частоте встречаемости
sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

# Сохраняем результат в файл readme.md
with open('readme.md', 'w') as file:
    for char, count in sorted_chars:
        file.write(f'{char}: {count}\n')
