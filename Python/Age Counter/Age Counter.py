def check_age(age):
  
  try:
    age = int(age)
    if age <= 0:
      return "Please enter a positive age."
    elif age > 120:
      return "Please enter a realistic age."
    elif age % 2 == 0:
      return "Your age is even."
    else:
      return "Your age is odd."
  except ValueError:
    return "Please enter a valid number for your age."

user_age = input("Enter your age: ")

result = check_age(user_age)
print(result)