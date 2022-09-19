def checkint(line):
    if line.isdigit() == True:
        return 'Строка является целым числом'
    else:
        return 'Строка не является целым числом'
line = input('Введите строку:')
print(checkint(line))