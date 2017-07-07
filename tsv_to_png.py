import os
import matplotlib.pyplot as plt
import Functions as func

#Считываем пользователей в список
user_list = []
file = open("users\\users_clear.txt", 'r')
user_list = file.read().splitlines()

#Считываем данные пользователей в список и строим графики
for user in user_list:
    file = open('users\\'+ user +'.tsv', 'r')
    List = []
    for line in file:
        S = line.split()
        List.append(S)
    # создание список точек
    list_point_x = []
    stop_point_x = []
    stop_point_y = []
    for i in List:
        list_point_x.append(i[1])
        if i[5] in ['1','2','3']:
            stop_point_x.append(i[1])
            stop_point_y.append(i[2])
    list_point_y = []
    for i in List:
        list_point_y.append(i[2])
    #постороение графика
    fig = plt.figure()
    plt.plot(list_point_x, list_point_y)
    plt.scatter(list_point_x, list_point_y, 25)
    plt.scatter(stop_point_x, stop_point_y, 55, 'r')
    func.save_pic(name='pic_' + user, fmt='png')
    #plt.show()
file.close()


