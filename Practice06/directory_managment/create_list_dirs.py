import os

#Creating Directories
os.chdir("C:\\Users\\Таир\\Desktop\\pp2-assignments\\Practice06\\directory_managment")
os.makedirs('First_Dir/Second_Dir/Third_Dir')

#Listing Directories and Files
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
    print()

#Searching files by extension
for file in os.listdir():
    if file.endswith(".py"):
        print(file)

