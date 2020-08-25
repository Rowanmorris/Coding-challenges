
def koa():
    words = str(input("Input word:")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print ()
    
    run_again = input("continue? ")
    print (run_again)

    if run_again == "no" or run_again == "No":
        print ("ok translator over")

    elif run_again == "Yes" or run_again == "yes":
        
        koa()
koa()