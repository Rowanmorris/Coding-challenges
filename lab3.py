n = int(input("Input a whole number: "))

def koa(n):
  print("number", "Squared", "Cubed")
  for i in range(1,n+1):
    if i <= n:
      print (i, i ** 2, i ** 3)

  run_again = input("Continue?")
  print (run_again)
    
  if run_again == "No" or run_again == "no":
    print ("Ok, excercise over")
    
  elif run_again == "Yes" or run_again == "yes":
    n = int(input('enter a whole number \n'))
  koa(n)

koa(n)