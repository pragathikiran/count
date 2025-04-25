file = open("file","r")
Counter = 0

content = file.read()

colist = content.split("\n")

for i in colist:
    if i:
        Counter += 1

print("this is the nimber of lines")
print(Counter)