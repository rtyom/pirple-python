#Fizz Buzz challenge

#Defining num range
St_num = 1
Fn_num = 100

#Defining function for prime checking
def checkForPrime(Number):
    if Number > 1:
        for i in range(2, Number):
            if (Number % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

#Making output
for List in range(St_num, Fn_num+1):

    if checkForPrime(List):
        attr = "PRIME!"
    else:
        attr = ""
        
    if List%3 == 0 and List%5 == 0:
        print(List, ": FizzBuzz", attr)
    elif List%3 == 0:
        print (List, ": Fizz", attr)
    elif List%5 == 0:
        print (List, ": Buzzz", attr)
    else:
        print(List, ":", attr)

