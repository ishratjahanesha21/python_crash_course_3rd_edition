# today we are going to learn about lists in python. Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
fruits = ["apple", "banana", "cherry"]
basket =["orange", "kiwi", "grapes"]
print(fruits)
print(basket)
# changing the value of a specific item in a list
# list are ordered, so you can change an item by its index
fruits[0] = "blueberry"
print(fruits)
# it is mutable - you can change items after creation
fruits[1]="mango"
print(fruits)

# it allows duplicate values
numberofpeople = ["John", "Peter", "John", "Mary"]
print(numberofpeople)
# it can store different data types

mixedlist = ["apple", 1, True, 3.14]
print(mixedlist)
studentGrades = [85, 90, 78, 92]
print(studentGrades)
item =[]
item =list()
print(item)

print (fruits[-1])
print (fruits[-2])

print (fruits[1:3])
basket = ["orange", "kiwi", "grapes", "banana", "mango", "watermelon", "pineapple", "papaya", "pear", "peach", "plum", "apricot", "coconut", "fig", "guava", "jackfruit", "lychee", "nectarine", "persimmon", "pomegranate"]
print (basket[3:10])
# output: ['banana', 'mango', 'watermelon', 'pineapple', 'papaya']
# adding item in list using appent method and the insert method
basketGrocery =["shampoo","soap", "toothpaste"]
basketGrocery.append("toothbrush")
print(basketGrocery)
basketGrocery.insert(0, "conditioner")
print(basketGrocery)
# extend method is used to add multiple items to the end of the list. It takes an iterable (like a list, tuple, or set) as an argument and adds each element of that iterable to the end of the list. 
bigBasket =[]
bigBasket.extend(basketGrocery)
bigBasket.extend(basket)
print(bigBasket)
# remove, pop
bigBasket.remove("shampoo")
print(bigBasket)
removed_item = basketGrocery.pop()
print(removed_item)
# print(bigBasket)
print(basketGrocery.count("soap"))
del basketGrocery 
print(bigBasket)
bigBasket.clear()

# some of the most common list methods are append(), insert(), extend(), remove(), pop(), clear(), index(), count(), sort(), and reverse()