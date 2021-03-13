# important_file = open('important_text.txt')
# print(important_file)
# print(important_file.read())

# not_important_file = open('just_text.txt')
# #.read(5) считает первые 5 символов текста
# #print(not_important_file.read())#текст - starting point
# #перезаписываем файл - test_changing
# not_important_file = open('just_text.txt', 'r+')
# not_important_file.write('test_changing_1')
# #print(not_important_file.read())
# not_important_file.close()
#readline() считывает строку до перехода на новую строку
#important_file = open('important_text.txt', 'r+')
########### операции читания файла ##############
#print(important_file.readline())
#print(important_file.readline())
#.readlines() считывает все строки и выдает их списком[]
#['Badgers;Snakes;3:0\n', 'Snakes;Gnomes;0:2']
#print(important_file.readlines())
#.seek()перемещает курсор в нужное место файла
#например .seek(10) перемещает курсор на 10 символ
#затем .read(3) печатает следующих 3 символов
#print(important_file.seek(10))
#print(important_file.read(3))
#прочитали первые 12 символов, потом курсор переместили на 25
#и прочитали еще 3 символа, можно считывать файл кусками
# print(important_file.read(12))
# print(important_file.seek(25))
# print(important_file.read(3))
# print(important_file.tell())
# important_file.close()

# ########### операции записи в файл ##############
# important_file = open('important_text.txt', 'a')
# #добавляем строчку в конец 'Enter some string'
# important_file.write('Enter some string\n')
# important_file.close()
# #.writelines() ожидает коллекцию [] и позволяет
# # добавить несколько строк сразу
# important_file = open('important_text.txt', 'a')
# important_file.writelines([
#     'Spam;Eggs;3:0\n'
#     'some new team\n'
# ])
# important_file.close()

# #задача: считать файл sport_teams.txt и сделать
# #таблицу по забитым голам по каждой команде
#
#создаем пустой словарь
results = {}
scores = open('sport_teams.txt')#открываем для чтения
for line in scores.readlines():
    team1, team2, score = line.split(';')
#разбиваем каждую строку по ; и распокавываем
#соответственно результат по team1, team2, score
    team1_score, team2_score = score.split(':')
#разбиваем результат по :
    results.setdefault(team1, 0)
    results.setdefault(team2, 0)
#метод словаря .setdefault() возвращает значение ключа либо
#если этого ключа нету то он его создает. При помощи него
# можем удостоверится что ключ существует и мы не
# перезаписываем чей-то результат
    results[team1] += int(team1_score)
    results[team2] += int(team2_score)

print(results)






















