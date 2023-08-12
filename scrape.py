import csv

f = open("test.txt", "r")
dict1 = {}
list1 = []
lines = f.readlines()
for i in lines:

    if (i[0].isdigit() or i[1].isdigit()) and (i[2] == '.' or i[1] == '.'):

        question = i
        list1 = []
    elif i[0] == "(" and i[1] in 'abcd' and i[2] == ')':
        print(i)
        option = i[3:]
        list1.append(option)
        dict1[question] = list1
    else:
        question = question + i


f.close()
print(dict1)

f = open("test3.csv", "w")
w = csv.writer(f)
for key in dict1:
    l1 = [key]
    l1.extend(dict1[key])
    w.writerow(l1)
