#print hello world
print("Hello World!")

#show datatype
name = "Aritra"
age = 20
height = 5.10
is_Student = True
print(type(name),type(age),type(height),type(is_Student))

#enter and print your name
name = input("Enter your name: ")
print("Your name: ",name)

#perform addition, subtraction, multiplication, division and modulo
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add = a+b
sub = a-b
mul = a*b
div = a/b
mod = a%b
print("Addition: ",add)
print("Subtraction: ",sub)
print("Multiplication: ",mul)
print("Division: ",div)
print("Modulo: ",mod)

#check number is positive, negative or 0
n = int(input("Enter a number: "))
if (n<0):
  print("Negative number")
elif (n>0):
  print("Positive number")
else:
  print("Zero")

#swap 2 numbers
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
a = a+b
b = a-b
a = a-b
print("1st number: ",a)
print("2nd number: ",b)

#check even odd
n = int(input("Enter a number: "))
if (n%2==0):
  print("Even number")
else:
  print("Odd number")

#leap year
year = int(input("Enter a year: "))
if (year%4==0 and year%100!=0 or year%400==0):
  print("Leap year")
else:
  print("Not a leap year")

#factorial
n = int(input("Enter a number: "))
s=1
for i in range(1,n+1):
  s = s*i
print("The factorial is: ",s)

#fibonacci series
n = int(input("Enter the range: "))
a = 0
b = 1
print(a)
print(b)
for i in range(2,n):
  c = a+b
  print(c)
  a = b
  b = c
  