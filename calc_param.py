import Functions as func

#Считываем файл в список
List = func.file_to_list('users\\12625231592051479902500977.tsv', 'r', -1, 0)

#вычисления значений T, L, Vcp
time1 = int(List[0][6])
time2 = 0
time = 0
d = 0
T = 0
last_point_x = float(List[0][1])
last_point_y = float(List[0][2])
L = 0.0
l = 0.0
Vcp = 0.0
Vmax = 0.0
i_start = -1
list_T = []
list_L = []
list_Vcp = []
list_Vmax = []
list_delta = []
list_T_yd = []
for i,line in enumerate(List):
    if i == 0:
        continue
    time2 = int(line[6])
    d = time2 - time1
    T += d
    if d == 0:
        continue
    time1 = int(line[6])
    l = (((float(List[i][1])-last_point_x))**2 + ((float(List[i][2])-last_point_y))**2)**(1/2)
    L += l
    Vmax_tmp = l / d
    if Vmax < Vmax_tmp:
        Vmax = Vmax_tmp
    last_point_x = float(List[i][1])
    last_point_y = float(List[i][2])
    if line[5] in ['1','2','3']:
        delta = d
        list_delta.append(delta)
        list_T_yd.append(int(List[i + 1][6]) - int(List[i][6]))
    if d > 500:
        T = round(T/1000, 3)
        print('T = ' + str(T) + '\t')
        L = round(L,3)
        print('L = ' + str(L) + '\t')
        Vcp = round(L / T, 3)
        print('Vcp = ' + str(Vcp) + '\t')
        print('Vmax = ' + str(round(Vmax*1000,3)) + '\t')
        list_T.append(T)
        list_L.append(L)
        list_Vcp.append(Vcp)
        list_Vmax.append(Vmax)
        T = 0
        L = 0
        Vcp = 0
        Vmax_tmp = 0.0
        Vmax = 0.0
        i_start = i
        print('\n')

print(list_delta)
print(list_T_yd)
#list_delta.sort()
#print(list_delta)
print('-------------')


