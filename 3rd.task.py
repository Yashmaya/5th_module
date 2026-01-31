user_input = int(input("enter the Number for check :"))
for i in range(2, user_input):

    if user_input % i == 0:
        print("Given number is not a prime number")
        break
else:
    print("Given number is a prime number")