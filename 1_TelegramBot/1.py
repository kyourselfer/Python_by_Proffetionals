if __name__ == '__main__':
    import math

#
# str1 = ' Vasilyy Petro   23  '
# print(str1.strip())
#
# for x in str1.strip():
#     print(x, x.isdigit())
# print('---\n')
# d1 = 3.5
# print('{}\nround = {} округляет в < или > \n'
#       'floor = {}(округляет вниз или отбрасывает целую часть числа)\n'
#       'ceil = {} округляет вверх'.format(d1, round(d1), math.floor(d1), math.ceil(d1)))
# print('\n\t--HW--')
# a = 2
# b = 4.5
# # c = 6.5
# print(float(a + b))
# print('\n\t--HW--')
# v = int(input('Enter digit between 1 and 10: '))
# print(v + 10)
# print('\n\t--HW--')
# name = input('Ent y name: ')
# print('Hi {}. How are you?'.format(name))
# print('\n\t--HW--')
# print(bool(1),bool(' '),bool(0))

# dict1 = {'Vendor': 'KIA', 'Model': 'Rio'}
# print(dict1.get('Vendor'))
# print(dict1.get('discount', 'Sorry but No.'))
# for key, value in dict1.items():
#     print(key, value)
#
# try:
#     del dict1['Vendor1']
# except KeyError:
#     pass
# print(dict1)

list1 = [2, 3, 4, 5, 6, 7]
print(list1)
list1.append('Python')
print(list1[0], list1[len(list1) - 1])
print(list1[1:4])
print(len(list1))
# try:
#     list2 = [x for x in list1 if x == int(x)]
#     print(list2)
# except TypeError:
#     print('type')

# for x in list1:
#     if x == 6:
#         print(list1.index(x))

str1 = [2, 3, 4, 5, 6, 7]

for x in str1:
    print(x, x.isdigit())
