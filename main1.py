from si import simple_interest

#input from user
P = int(input("Enter Principal amount: "))
R = int(input("Enter Rate of interest: "))
T = int(input("Enter Time: "))

#calling function from si module
final_result = simple_interest(P, R, T)

#display the result
print("Simple Interest is:", final_result)