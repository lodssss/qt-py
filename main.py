import os

converter = os.path.dirname(__file__)
print('\n', converter, '\n')

project = input('project name: ')
print(project, '\n') 

main_dir = converter.removesuffix('qt-py')
print(main_dir, '\n') 

target = f'{main_dir}{project}\\'
print(target, '\n')

ui = input('ui name: ')

path = f'{converter}\\venv\Scripts\pyuic6.exe -x {target}{ui}.ui'

print(path)
os.system(path)

input()
