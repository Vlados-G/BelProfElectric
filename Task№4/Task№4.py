# Task№4

import json
from datetime import datetime

# Открываем файл и загружаем его содержимое в переменную
with open('file.json', 'r') as file:
    data = json.load(file)


# Обходим структуру данных рекурсивно для поиска и замены всех полей "updated"
def replace_updated_fields(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'updated':
                obj[key] = datetime.now().isoformat()
            else:
                replace_updated_fields(value)
    elif isinstance(obj, list):
        for item in obj:
            replace_updated_fields(item)


# Заменяем все поля "updated" на текущую дату и время
replace_updated_fields(data)

# Сохраняем обновленный файл
with open('file.json', 'w') as file:
    json.dump(data, file, indent=2)
