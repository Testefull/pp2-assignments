#Reading and printing file data

with open('sample.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)