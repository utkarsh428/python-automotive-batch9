print("Get max, min, swap value of variables")
print("\n 1.Max \n 2.Min \n 3.Swap")
a,b = map(int,input("enter two numbers ").split(","))
          #34, 23
choice = int(input("Enter your choice"))
if(choice==1):
          print(max(a,b))
elif(choice==2):
          print(min(a,b))
elif(choice==3):
          a,b = b,a
          print("after swaping %d %d " %(a,b)) #23,34
else:
          print("Invalid choice")