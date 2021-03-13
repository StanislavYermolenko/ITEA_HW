#системная переменная
import os
#os.environ словарь где хранятся все переменные среды
#print(os.environ['MY_IMPORTANT_VAR'])
login = os.environ['MY_IMPORTANT_VAR']
password = os.environ['PASSWORD']
#создаем в терминале export MY_IMPORTANT_VAR='123456'
#export PASSWORD='123456789' и используем в коде
#например get_data(login, password)
