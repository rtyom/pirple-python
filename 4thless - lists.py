myUniqueList = ["a","b","c"]
myLeftovers = []

print ("Are you already in this list?")
print (myUniqueList)
    
a = input()

def rejLover(a):
    if (a in myUniqueList):   
        myLeftovers.append(a)
        return True
    
def addLover(a):
    if (a in myUniqueList):
        return False
    else:
        myUniqueList.append(a)
    return True

if (rejLover(a)):
    print ("Darling, youre in the base! I'm adding you to old base")
    print (myLeftovers)
    print ("Ciao...")
    
if (addLover(a)):
    print ("Darling, youre not exists in my lover's list. You will be the next!")
    print (myUniqueList)
    print ("You're welcome!")

 
