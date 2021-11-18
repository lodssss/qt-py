import os

converter = os.path.dirname(__file__)
main_dir = converter.removesuffix('qt-py')

project = input('project name: ')
ui = input('ui name: ')

target = f'{main_dir}{project}\\'

path = f'{converter}\\venv\Scripts\pyuic6.exe -x {target}{ui}.ui'

os.system(path)

input()