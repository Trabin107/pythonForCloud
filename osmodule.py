#with the use of os module we can check if the file exists or not
import os
if os.path.exists("text.txt"):
    f = open("text.txt", "r")
    print(f.read())
    f.close()
    print("File exists")
else:
    print("File does not exists")
    