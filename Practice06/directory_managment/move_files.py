import os

#Creatng files
try:
    f1 = os.open('file1.txt', os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    f2 = os.open('file2.txt', os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    f3 = os.open('file3.txt', os.O_CREAT | os.O_EXCL | os.O_WRONLY)

    os.close(f1)
    os.close(f2)
    os.close(f3)

    print("Files Created")

except FileExistsError:
    print("Files Already Exist")

#Moving Files
os.rename('file1.txt', 'First_Dir/file1.txt')
os.rename('file2.txt', 'First_Dir/Second_Dir/file2.txt')
os.rename('file3.txt', 'First_Dir/Second_Dir/Third_Dir/file3.txt')
