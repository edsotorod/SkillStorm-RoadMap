'''
Topic - Functions

def hello_world():
  print("Hello World")

hello_world()
'''

'''
Topic - Parameters, Arguments, and Return

def addition(num1,num2):
  return num1 + num2

def subtraction(num1,num2):
  return num1 - num2

def multiplication(num1,num2):
  return num1 * num2

def divition(num1,num2):
  if num2 == 0:
    return "Unable to divide by 0"
  return num1 / num2

addition(2,3)
subtraction(5,3)
multiplication(3,4)
divition(6,2)
'''

'''
Topic - Built-in Functions

def min(list):
  smallest = None
  
  if len(list) > 0:
    smallest = list[0]
  
  for x in list:
    if smallest > x:
      smallest = x
  
  return smallest

print(min([-1,2,3,4,5,1]))
'''

'''
Topic - Modules
'''