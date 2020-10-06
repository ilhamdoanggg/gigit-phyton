my_list = [1,2,3,4,6,7,]
new_MyList = list(filter(lambda x:(x%2==0), my_list))
new_MyList1 = list(map(lambda x:x*4, my_list))
print(my_list)
listA = new_MyList1
print(listA)
