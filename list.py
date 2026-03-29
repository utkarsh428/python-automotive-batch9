#List = used to store multiple items in a single variable
food = ["pizza", "hamburger", "hotdog", "spaghetti"]
print(food[0]) #pizza
print(food[3]) #spaghetti

food[0]= "sushi"
print(food[0])#pizza updated to sushi

food.append("ice cream") 
food.remove("hotdog")
food.pop() #removes last element
food.pop(1) #remove element indexwise
food.insert(0, "cake") 
food.clear() #clear list

for i in food:
    print(i)