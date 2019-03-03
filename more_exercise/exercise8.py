list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
new_list=[]
# def lists(list1,list2):
# 	for i in list1:
# 		if i not in list2:
# 			list2.append(i)
# 	print (list2)
# lists(list1,list2)
for i  in list1:
	for j in list2:
		if j  not in list1:
			list1.append(j)
print list1