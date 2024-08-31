try :
    num1=int(input("Enter a number"))
    num2=int(input("Enter a number"))
    result=num1/num2
    print("Result is :",result)

except ZeroDivisionError:
    print("Divison by zero is not allowed")
except ValueError:
    print("Please enter a numerical Value")
except NameError as ex:
    print("Exception: ",ex)
except:
    print("An error Occured")
finally:
    print("I will execute no matter what")    

