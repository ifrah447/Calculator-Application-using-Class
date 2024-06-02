import math
class calci(object):

    def add(self,num1,num2):
        answer = num1 + num2
        print('Sum = ',answer)
    def sub(self,num1,num2):
        answer = num1 - num2
        print('Difference = ',answer)
    def mul(self,num1,num2):
        answer = num1 * num2
        print('Product = ',answer)
    def div(self,num1,num2):
        answer = num1 / num2
        print('Quotient = ',answer)
    def squareroot(self,num):
        answer = math.sqrt(num)
        print("Square Root(%f) = %f " %(num,answer))
    def pie(self):
        print( 'pi = ',math.pi)
    def powerof(self,num,raiseby):
        answer = math.pow(num,raiseby)
        print("%f ^ (%f) = %f" %(num,raiseby,answer) )
calc = calci()
print('welcome to casio')
print("Here's a list of choices")
print('*'*60)
print("1 : Addition  \t\t   ")
print("2 : Subtraction \t ")
print("3 : Multiplication\t   ")
print("4 : Division  \t\t   ")
print("5 : Sine in radians\t")
print("6 : Coisne in radians\t")
print("7 : Tan in radians\t ")
print("8 : Cosecant in radians")
print("9 : Secant in radians\t")
print("10 : Square root\t")
print("11 :  Power of\t")
print('*'*60)
choice = ""
while True:
    try:
        choice = int(input('enter a number of your choice from the above list : '))
    except:
        print("Enter a valid number")
    if choice == 1:
        n1 = float(input('enter the first number to add : '))
        n2 = float(input('enter the second number to add : '))
        calc.add(n1,n2)
    elif choice == 2:
        n1 = float(input('enter the first number to subtract : '))
        n2 = float(input('enter the second number to subtract : '))
        calc.sub(n1,n2)
    elif choice == 3:
        n1 = float(input('enter the first number to multiply : '))
        n2 = float(input('enter the second number to multiply : '))
        calc.mul(n1,n2)
    elif choice == 4:
        n1 = float(input('enter the first number to divide : '))
        n2 = float(input('enter the second number to divide : '))
        calc.div(n1,n2)
    elif choice == 5:
        n = float(input('enter a number to find its sine in rad: '))
        calc.sinrad(n)
    elif choice == 6:
        n = float(input('enter a number to find its cos in rad: '))
        calc.cosrad(n)
    elif choice == 7:
        n = float(input('enter a number to find its tan in rad : '))
        calc.tanrad(n)
    elif choice == 8:
        n = float(input('enter a number to find its cosec in rad : '))
        calc.cosecrad(n)
    elif choice == 9:
        n = float(input('enter a number to find its sec in rad : '))
        calc.secrad(n)
    elif choice == 10:
        n = float(input('enter a number to find its cot in rad : '))
        calc.squareroot(n)
    elif choice == 11:
        n=float(input('enter a number: '))
        po=float(input('enter its power: '))
        calc.powerof(n,po)
    else:
        print("WARNING : Enter a valid input from the list above")
