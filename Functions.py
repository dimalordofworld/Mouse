import os
import matplotlib.pyplot as plt

#Сохранение картинки
def save_pic(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './pictures/{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)

#Считываем файл в список списков(имя файла, как считывать, номер максимальной итерации для отладки, строки которые не нужно считывать)
def file_to_list(file_name, rw, stop_iter, *args):
    file = open(file_name, rw)
    List = []
    for i, line in enumerate(file):
        if i == stop_iter:
            break
        if i in args:
            continue
        S = line.split()
        List.append(S)
    file.close()
    return List

