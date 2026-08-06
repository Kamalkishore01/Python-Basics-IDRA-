num1=float(input("Enter the 1st no: "))
num2= float(input("Enter the 2nd no: "))


#Arithmetic Operations;;
addition= num1+num2
subtraction=num1-num2
multiplication=num1*num2
division= num1/num2
exponention= num1**num2
floor_division= num1//num2
modulus= num1%num2

#Display the result

print("\n----- Arithmetic Operations -----")
#The f is used to create an f-string, 
# which allows variables and expressions 
# to be inserted directly into a string using curly braces {}

print(f"Addition (+): {num1} + {num2} = {addition}")
print(f"Subtraction (-): {num1} - {num2} = {subtraction}")
print(f"Multiplication(*): {num1} * {num2}= {multiplication}")
print(f"division(/): {num1}/{num2}= {division}")
print(f"exponention(**): {num1}**{num2}= {exponention}")
print(f"floor_division(//): {num1}//{num2}={floor_division}")
print(f"modulus(%): {num1}%{num2}={modulus}")