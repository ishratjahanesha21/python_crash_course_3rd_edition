cars=["bmw", "mercedes", "audi", "porsche"]
# make all car name in title case but in case of bmw we want to make it in uppercase.
for car in cars:
    if car=="bmw":
        print(car.upper())
    else:
        print(car.title())


# ALL the if statment has two result that is boolen . bollen have two value True or False. if the condition is true then it will execute the code inside the if block and if the condition is false then it will execute the code inside the else block. 
# so true and false are conditional test 
#   oparetion parameters ARE  used to compare the values and return a boolean value. there are six conditional test operators that are used to compare the values.
# 1. Equal to (==) 2. Not equal to (!=) 3. Greater than (>) 4. Less than (<) 5. Greater than or equal to (>=) 6. Less than or equal to (<=) , and the logical operators (and, or, not) to combine these conditions. add && or || and not are used to combine the conditions.
magicians = ["alisha", "ben", "charlie", "diana"]
for magician in magicians:
    print(magician)
    
# 1. Even or Odd ⭐ (Easy)
giving_number = int(input("Enter a number: "))
if giving_number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Age Category ⭐ (Easy)    # 
giving_age = int(input("Enter your age: "))
if (giving_age < 13):
    print("You are a child.")

elif (giving_age >= 13 and giving_age <= 19):
    print("You are a teenager.")

elif(giving_age >= 20 and giving_age <= 59):
    print("You are an adult.")
elif(giving_age >= 60):
    print("You are a senior citizen.")   


    # 
#  check the positive and nagative number 
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")