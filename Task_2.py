my_file = open('Task 2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('Task 2.txt', 'r')
content = my_file.readlines()
print(f'Кол-во строк в файле - {len(content)}')
my_file = open('Task 2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Кол-во символов {i + 1} - ой строки {len(content[i])}')
my_file = open('Task 2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее кол-во слов - {len(content)}')
my_file.close()
