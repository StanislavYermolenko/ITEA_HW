#по сути пакеты являются набором модулей или
#других пакетов __init__

from modules import factorial, get_handle
from my_package.f import *
bar()
print(factorial(6))
q = get_handle()
print(q.upper())
