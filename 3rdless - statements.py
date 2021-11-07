#declaring variables
a = 5
b = 4
c = "5"

#declaring function for comparsion
def compABC(a,b,c):

    #passing incoming data as integers only
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a == b or a == c or b == c or c == a:
        return True
    else:
        return False

#making output
if compABC(a,b,c):
    print ("Some of three varibales is equal")
else:
    print ("No equals")

