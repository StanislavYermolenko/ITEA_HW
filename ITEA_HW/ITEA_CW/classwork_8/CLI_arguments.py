# #передача файла скрипту на исполнение
# file_path = input('Input a file path: ')
# get_info = open(file_path)
# print(get_info.read())

# import sys
# print(sys.argv)

# import sys
# results = {}
# filepath = sys.argv[1]
# scores = open('sport_teams.txt')
# for line in scores.readlines():
#     team1, team2, score = line.split(';')
#     team1_score, team2_score = score.split(':')
#     results.setdefault(team1, 0)
#     results.setdefault(team2, 0)
#     results[team1] += int(team1_score)
#     results[team2] += int(team2_score)
#
# print(results)

#отобрать все части argv, начинающиеся на --
#params = filter(lambda x: x.startwith('--'), sys.argv)

#модуль argparse предназначен для сложных аргументов

#import argparse

#системная переменная PATH позволяет находить любые программы










