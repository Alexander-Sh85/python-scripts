# скрипт меняет версию продакшн строндор.ру. Используется в тимсити как дополнительный параметр
import sys

filename = "docker-compose.yaml"  # путь к файлу
search_phrase = "frontend-strondorru-node:" # Ищем строку
replacement = sys.argv[1]  # заменить на эти символы
f = False # Делаем 1 раз чтоб не зацепить девстрондор

# Открываем файл на чтение
with open(filename, 'r') as file:
    lines = file.readlines()

# Ищем фразу и производим замену
new_lines = []
for line in lines:
    if (search_phrase in line) and (not f):
        # Находим позицию символа ":" в строке
        pos = line.index(":") + 57
        # Заменяем символы после ":" на указанную строку
        new_line = line[:pos+1] + replacement + "\n"
        # Добавляем измененную строку в новый список строк
        new_lines.append(new_line)
        f = True
    else:
        new_lines.append(line)

with open(filename, 'w') as file:
        file.writelines(new_lines)