#1 no 
def divide(a,b):
    quo = a // b
   # rem = a - (b * quo)
    rem = a %b
    return quo , rem

n1 = int(input("enter num :"))
n2 = int(input("enter num :"))
res = divide(n1,n2)
print(res)

q , r = divide(n1,n2)
print (q , r)

#2 no

nums = [1, 2, 2, 3, 4, 4, 4, 5]
uni = set(nums)
print(uni)
print(len(uni))

#3 no
c1 = input("Enter student 1 courses , separated by comma: ")
c2 = input("Enter student 2 courses , separated by comma: ")

s1_c1 = c1.split(",")
s1_c1_uni = set(s1_c1)

s2_c2 = c2.split(",")
s2_c2_uni = set(s2_c2)

print("Courses both are taking(intersection): ", s1_c1_uni & s2_c2_uni)
print("Courses only the student is taking(diff): ", s1_c1_uni - s2_c2_uni)
print("All Courses (union): ", s1_c1_uni | s2_c2_uni)

# 4 no
s = set()

for i in range(5):
    num = int(input("Enter numb:"))
    s.add(num)

print(s)