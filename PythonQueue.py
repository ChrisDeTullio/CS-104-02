names = []
for x in range(10):
    acceptedName=str(input("Please enter your name: "))
    names.append(acceptedName)
print(names)
for y in range(10):
    print(names.pop(0))
print(names)
    
