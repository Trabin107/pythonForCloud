# list filter example to list values greater than 15 using the lambda function
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
myfilterlist = list(filter(lambda x: x > 15, list1))
print(myfilterlist)

