#simple read file example
f=open("text.txt", "r")
print(f.read())
f.close()

# #lets try the write mode
# f = open("text.txt", "w")
# print(f.write("This is a new line"))
# f.close()

#we can read the file with the specific encoding
f = open("text.txt", "r", encoding='utf-8')
print(f.read())
f.close()

#loop through the eaach file
f = open("text.txt", "r")
for x in f:
    print("Line: ", x)
f.close()