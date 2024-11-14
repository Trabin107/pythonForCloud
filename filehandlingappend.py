#using the append mode 
f = open("text.txt", "a")
f.write("i am appending this line")
f.close()

#write method will overwrite the existing content of the file
#simialr to checking if the file exists or not, if the file exits we can remove 
import os
os.remove("text.txt")