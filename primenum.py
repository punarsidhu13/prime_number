# Prime number
 
def prime_number(num):
    if num == 1:
        print("It is not a prime number")
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print("This is not a prime number")
                break
            else:
                print("This is a prime number")

    else:
        print("This is not a prime number")


n=int(input("Enter a number:- \n "))
prime_number(n)