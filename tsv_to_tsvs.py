import os
import Functions as func

#1479841196.966 (10з.3з)
#[0'id',1'client_x',2'client_y',3'page_x',4'page_y',5'which',6'created',7'user', 'width', 'height', 'availWidth', 'availHeight']

#Считываем файл в список
List = func.file_to_list('mldm_mouse_data.tsv', 'r', -1, 0)

#отчищаем спиок
for line in List:
    if line[5] in ['1','2','3']:
        continue
    line.insert(5,'0')

#получение списка всех пользователей и запись этого списка в файл
user_list_tmp = set()
user_list = []
for line in List:
    user_list_tmp.add(line[7])
user_list = user_list_tmp
f = open("users\\users.txt", 'w')
i = 0
for user in user_list:
    if i == 0:
        f.write(str(user))
        i += 1
        continue
    f.write("\n" + str(user))
f.close()
print(user_list)

#создание отдельного файла для каждого пользователя
for user in user_list:
    user_name = str(user)
    f = open("users\\" + user_name + ".tsv", 'w')
    i = -1
    j = -1
    for line in List:
        i += 1
        if List[i][7] == user_name:
            j += 1
            if j == 0:
                for elem in List[i]:
                    f.write(str(elem) + "\t")
                continue
            f.write("\n")
            for elem in List[i]:
                f.write(str(elem) + "\t")
    f.close()

#отчистка данных (удаление всех пользователей, у которых меньше 150 записей, у которых нет нажатий или все нажатия)
user_list_clear = []
for user in user_list:
    flag1 = 1 #все 1 в столбце which
    flag0 = 1 #все 0 в столбце which
    count_line = 0
    user_name = str(user)
    List = func.file_to_list("users\\" + user_name + ".tsv", 'r', -1)
    for i,line in enumerate(List):
        count_line += 1
        if line[5] == '0':
            flag1 = 0
        if line[5] in ['1','2','3']:
            flag0 = 0
    if count_line < 150 or flag0 == 1 or flag1 == 1:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "users\\" + user_name + ".tsv")
        os.remove(path)
        continue
    user_list_clear.append(user_name)

#запись в файл отчищенного списка пользователей
f = open("users\\users_clear.txt", 'w')
i = 0
for user in user_list_clear:
    if i == 0:
        f.write(str(user))
        i += 1
        continue
    f.write("\n" + str(user))
f.close()
print(len(user_list_clear))
