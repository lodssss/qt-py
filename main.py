import os

converter = os.path.dirname(__file__) # change commit name to converter
project = input('project name: ') # change name and commit to target
main_dir = str.removesuffix(converter, 'qt_to_py')
target = main_dir + '\\' + project + '\\'
print(target)
ui = input('ui name: ')

path = "{}\\venv\Scripts\pyuic6.exe -x {}{}.ui".format(converter, target, ui)

print(path)
os.system(path)

input()