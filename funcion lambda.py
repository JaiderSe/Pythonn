any_list = [1, 2, 3, 4]
even_list = list(map(lambda x: x+1 if x%2==0 else x+0, any_list))
#even_list = list(map(lambda n: n | 1, any_list))
print(even_list)