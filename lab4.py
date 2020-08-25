num = int(input("Enter a number between 1 and 10: "))

 
def koa(num):
  factorial = 1
  if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
  elif num == 0:
    print("The factorial of 0 is 1")
  else:
   for i in range(1,num + 1):
       factorial = factorial*i
  print("The factorial of",num,"is",factorial)

  run_again = input("continue? ")
  print (run_again)

  if run_again == "no" or run_again == "No":
    print ("ok calculator over")

  elif run_again == "Yes" or run_again == "yes":
    num = int(input('enter a number between 1 and 10 \n'))
    koa(num)

koa(num)