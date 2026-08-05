# 1 no problem
a = int (input("Enter a number: "))
b = int (input("Enter another number: "))
result = a + b
print(" The result of sum:" ,result)

diff  = a - b
print(" The result of difference:" ,diff)

pro = a * b
print("The result of product: ",pro)

div = a // b
print("The result of division:", div)


#2 no problem
age = int(input("Enter your age: "))
if age >= 65:
    print("Senior")
elif age < 11 :
    print("Minor")
elif age <=18:
    print ("Teen")
else :
    print ("Adult")

#3 no 
num = int(input("Enter a number: "))

if (num % 2)==0 :
    print("Even")
else:
    print("Odd")

# 4 no 

temp = float(input("Enter the temperature as celsius: "))
f = (temp * (9 / 5) + 32)
print("The temperature in Farhenheit :", f)

 