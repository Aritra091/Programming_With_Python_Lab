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