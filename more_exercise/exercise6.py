# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# # print (set(list1) & set(list2))  this is one line code to solve this question.
# def common(list1,list2):
# 	lista=[]
# 	for i in list1:
# 		if i in list2:
# 			listq.append(i)
# 		print (lista)

list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
new_list=[]
for i in list1 or i in list2:
	if i not in new_list:
		new_list.append(i)
print (new_list)