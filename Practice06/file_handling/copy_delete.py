#Copying using shutil
import shutil, os

shutil.copy('sample.txt', 'sample_copy.txt')

#Safe deletion of the file
file_path = 'C:\\Users\\Таир\\Desktop\\pp2-assignments\\Practice06\\file_handling\\sample.txt'

if os.path.exists(file_path):
    os.remove(file_path)
    print("File Deleted")
else:
    print("Not found")