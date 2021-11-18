import os


this_path = os.path.dirname(__file__)
main_dir = this_path.removesuffix('qt-py')

project = input('project name: ')
ui = input('ui name: ')

target = f'{main_dir}{project}\\'

path = f'{this_path}\\venv\Scripts\pyuic6.exe -x {target}{ui}.ui'

os.system(path)

convert = input('''
do again OR convert to .txt?
| A for again | C for convert |

''') 

if convert in 'Aa':
    pass # func for again
elif convert in "Cc":
    pass # func for convert
else: pass # loop the input

path = f'{this_path}\\venv\Scripts\pyuic6.exe -x {target}{ui}.ui -o {ui}.txt'

os.system(path)

open_file = f'{this_path}\{ui}.txt'
os.system(open_file)

input('press to delete file and start again\n\n')
os.remove(open_file)