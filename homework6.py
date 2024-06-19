my_dict = {'Anton': 1993, 'Viktor': 1934, 'Nikolai': 1999, 'Vladimir': 1990}
print(my_dict)
print(my_dict ['Nikolai'])
my_dict ['Viktoria'] = 2001
print(my_dict)
my_dict.update({'Sasha': 1996, 'Max': 1996})
print(my_dict)
a = my_dict.pop('Anton')
print(my_dict)
print(a)

my_set = {1, 2, 3, 4, 1, 'Hello', 2, True, 3, 5, 1, 2, 6}
print(my_set)
print(my_set.add(12))
print(my_set.add(14))
print(my_set)
print(my_set.discard(4))
print(my_set)