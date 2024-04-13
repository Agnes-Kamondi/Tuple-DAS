#creating a tuple                                                                                                                                                                                        
fruits = ("banana","orange","pineapple","strawberry","pears")
print(fruits)

#accessing items using slicing
print(fruits[2])
print(fruits[1:4])
print(fruits[0:3])
print(fruits[-4:-1])

#adding items in a tuple
#1 changing into a list
fruit = list(fruits)
print(fruit)
fruit[0]="watermelon"
fruit.append("kiwi")
fruits=tuple(fruit)
print(fruits)

#2adding a tuple to a tuple
y=("apple",)
fruits+=y
print(fruits)

#determining the maximum value 
x = list(fruits)
print(max(x))
fruits=tuple(x)
print(fruits)


#finding the length
print(len(fruits))

#removing items from a tuple
h = list(fruits)
print(h)
h.remove("kiwi")
fruits = tuple(h)
print(fruits)

#removing all the items
# del(fruits)





 


