import Functions as func

user_list = []
file = open("users\\users_clear.txt", 'r')
user_list = file.read().splitlines()

user_list = ['6969440262783551479887094715']
user_list1 = []
for user in user_list:
    count_line = 0
    user_name = str(user)
    List = func.file_to_list("users\\" + user_name + ".tsv", 'r', -1)
    for i,line in enumerate(List):
        count_line += 1
        if i == 0:
            continue
        if (int(List[i][6]) - 100000) > int(List[i - 1][6]):
            print(i)
            if count_line < 100:
                for j in List:
                    if

            #user_list1.append(user)

#print(user_list1)
#print(len(user_list1))
list = [6,5,4,3,2]
list.pop(0)
print(list)