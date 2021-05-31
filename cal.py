import  numpy
def add():
    num1=int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))
    return num1+num2;


def sub():
    num1 = int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))
    return num1-num2;

def multi():
    num1 = int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))
    return num1*num2;

def div():
    num1 = int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))
    return num1/num2;
def mod():
    num1 = int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))
    return num1%num2;


print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Mode")


op = int(input("enter operation number from above (1,2,3,4,5):"))
if (op==1):
   print( "addition: ",add());
elif(op==2):
    print("Substraction:", sub())

elif(op==3):
    print("Multiplication:", multi())

elif(op==4):
    print("division: ", div())

elif(op==5):
    print("MODE: ", mod())

else:
    print("invalid option...")





