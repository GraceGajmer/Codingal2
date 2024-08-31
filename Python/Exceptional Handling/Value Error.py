try :
    num=int(input("Enter any number"))
    print(num)
except ValueError as ex:
    print("Exception: ",ex)

print("I am outside the try Block")    