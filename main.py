x= input("Enter Value of x:")
y= input("Enter Value of y:")
z= input("Enter Value of z:")
temp = x
x=z
z= temp
temp = z
z=y
y= temp
print("value of x after swapping", x)
print("value of y after swapping", y)
print("value of z after swapping", z)