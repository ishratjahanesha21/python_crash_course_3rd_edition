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