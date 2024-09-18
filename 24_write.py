# with open('./text.txt', 'r+') as file:
with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('Nuevas cosas en este archivo\n')
    file.write('Otra línea\n')
    file.write('Otra más\n')