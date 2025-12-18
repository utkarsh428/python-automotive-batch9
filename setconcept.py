mySet = {"apple", "banana", "cherry", "apple",False,0,1,2}
mylist = ['a','b']
mySet2 = {'a','n'}
print(mylist)
#true = 1 
#false = 0
empty_set = set()
empty_dict = { }
print(type(empty_set))
mylist.add(10)
mylist.discard(10)
mySet.update(mylist)
count = len(mySet)
print(mySet | mySet2) #union
print(mySet & mySet2) #intersection
for fruit in mySet:
    print(fruit)
