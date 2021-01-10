
with open('1.txt', 'r', encoding="utf-8") as f1, open('2.txt', 'r', encoding="utf-8") as f2, open('3.txt', 'r', encoding="utf-8") as f3:
    file_1 = f1.readlines()
    file_2 = f2.readlines()
    file_3 = f3.readlines()

correct_location = {'1.txt': [len(file_1), file_1], '2.txt': [len(file_2), file_2], '3.txt': [len(file_3), file_3]}

for_sort = list(correct_location.values())
for_sort.sort()
for x in for_sort:
    count = 0
    for key, items in correct_location.items():
        if x[0] in items:
            new_file = open('new_file.txt', 'a+')
            new_file.write(str(f'\n{key}\n'))
            new_file.write(str(f'{x[0]}\n'))

    for y in x[-1]:
        count += 1
        for key, items in correct_location.items():
            if x[0] in items:
                new_line = f'Строка номер {count} из файла {key} ' + y
                new_file = open('new_file.txt', 'a+')
                new_file.write(new_line)
