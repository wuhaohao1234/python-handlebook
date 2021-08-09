import sys
from mymodule import say_hi, __version__

print('命令行的参数为: ')

for i in sys.argv:
  print(i)

print('\n',sys.path,'\n')

say_hi()

print(__version__)