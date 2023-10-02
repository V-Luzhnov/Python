print('Введите имя:')
name = input().upper()
for el in name:
    if not ((64 < ord(el) < 91) or (1039 < ord(el) < 1072)) and ord(el) != 32:
        print('В имени присутствуют недопустимые символы')
        break
