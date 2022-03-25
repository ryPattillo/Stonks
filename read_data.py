file = open("Data.txt","r")
print(file.readline())


for line in file:
    print(type(line))