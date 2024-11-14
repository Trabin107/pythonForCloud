#get the current working directory
import os
print(os.getcwd())

#change the current working directory
# import os
# print(os.chdir())

#list the files and directories in the current working directory
import os 
print(os.listdir())

#make a new directory
# import os
# print(os.mkdir("python"))

#remove a empty directory
# import os
# print(os.rmdir("python"))

# remove a directory which already has files in it
# import shutil
# print(shutil.rmtree("newdir"))

#rename a directory
import os
print(os.rename("python", "newdirectory"))

#moving all the file to a new directory
import shutil
print(shutil.move("test.txt", "newdirectory"))


