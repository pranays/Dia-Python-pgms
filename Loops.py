'''
This program generates Fibbonaci
'''
def Fibonacci():
  old = 0
  new = 1
  print(old)
  for i in range(10):
    print(new)
    res = new + old
    new = res
    old = new

'''
Reverse give number "123" becomes "321"
'''
def ReverseNum1():
  num = str(input("enter a num: "))
  res = [x for x in str(num)]
  res.reverse()
  for i in res:
    print(i, end="")

def ReverseNum2():
  num = 76542
  reverse_number = 0
  print("Given Number ", num)
  while num > 0:
      reminder = num % 10
      reverse_number = (reverse_number * 10) + reminder
      num = num // 10
  print("Revere Number ", reverse_number)

'''
This function calculates Factorial of given number.
'''
def Factorial():
  num = int(input("num: "))
  factorial = 1
  for i in range(1,num+1):
    factorial = factorial * i
  print(factorial)
