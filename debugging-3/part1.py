num_list_20=[]
def numbers_greater_than_twenty(num_list):
  counter = 0
  while counter < len(num_list):
    item = num_list[counter]
    counter+=1
    if item < 20:
      num_list_20.append(item)
  return (num_list_20)

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_20 = numbers_greater_than_twenty(num_list)

print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_20)