from operator import truediv

list = []

while True:
    inputs = input("enter the number or press enter to quit: ")

    if inputs == "":
        break

    list.append(int(inputs))
list.sort(reverse=True)
print(list[:5])
