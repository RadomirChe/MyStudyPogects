list1 = ['Ukraine', 'Spain', 'Italy']
dict_sample = {list1[0]: 'Kyiv', list1[1]: 'Madrid', list1[2]: 'Rome'}
#print(list1[0], ': ', dict_sample[list1[0]], sep='')
#print(list1[1], ': ', dict_sample[list1[1]], sep='')
#print(list1[2], ': ', dict_sample[list1[2]], sep='')
for key, value in dict_sample.items(): print(f" {key}: {value} ")
#print(dict_sample.items())