#!/bin/python3
from functools import reduce
import operator
from pyfiglet import Figlet


def banner(text):
        custom_fig = Figlet(font='graffiti')
        print(custom_fig.renderText(text))

banner("Calculator")
print("                                                         V1.0")
print("                                                         Coded by : Vu1n3rab1e")
numbers = []
res = 0
print("==================================================================================================")
print("""\nWhich type of calculator would you like to use?\n1.Basic\n2.Experimental\nNOTE:Experimental Version is not completed and is expected to have bugs/errors.""")
option = int(input("Choose an option : "))
print("==================================================================================================")
if (option == 1 or option == 2):
        if option == 1:
                while True:
                        print("\n1.Addition")
                        print("2.Subtraction")
                        print("3.Multiplication")
                        print("4.Division")
                        print("5.Square Root")
                        #print("Sin, Cos, Tan")
                        print("6.Exit")

                        choice = int(input("Enter Your Choice: "))
                        print("==================================================================================================")
                        if (choice >=1 and choice <=4):
                                print("To calculate with the result of previous calculation, Just enter res in the field of number.\nEg: Consider the value of result as 10 and the choice as Addition for the sake of this example.\nres\n10\nResult= 20\nEnter Two Numbers: ")
                                num1 = input()
                                num2 = input()

                                if (num1 == "res"):
                                        num1 = float(res)
                                        num2 = float(num2)
                                        if choice == 1:
                                                res = num1 + num2
                                                print("Sum of {} and {} = {}\n==================================================================================================".format(num1,num2,res))
                                        elif choice == 2:
                                                res = num1 - num2
                                                print("Difference of {} and {} = {}\n==================================================================================================".format(num2,num1,res))
                                        elif choice == 3:
                                                res = (num1 * num2)
                                                print("Product of {} and {} = {} \n==================================================================================================".format(num1,num2,res))
                                        elif choice == 4:
                                                res = (num1 / num2)
                                                print("{} Divided by {} = {} \n==================================================================================================".format(num1,num2,res))


                                elif (num2 == "res"):
                                        num1 = float(num1)
                                        num2 = float(res)
                                        if choice == 1:
                                                res = num1 + num2
                                                print("Sum of {} and {} = {}\n==================================================================================================".format(num1,num2,res))
                                        elif choice == 2:
                                                res = num1 - num2
                                                print("Difference of {} and {} = {}\n==================================================================================================".format(num2,num1,res))
                                        elif choice == 3:
                                                res = (num1 * num2)
                                                print("Product of {} and {} = {} \n==================================================================================================".format(num1,num2,res))
                                        elif choice == 4:
                                                res = (num1 / num2)
                                                print("{} Divided by {} = {} \n==================================================================================================".format(num1,num2,res))

                                else:
                                        num1 = float(num1)
                                        num2 = float(num2)
                                        if choice == 1:
                                                res = num1 + num2
                                                print("Sum of {} and {} = {}\n==================================================================================================".format(num1,num2,res))
                                        elif choice == 2:
                                                res = num1 - num2
                                                print("Difference of {} and {} = {}\n==================================================================================================".format(num2,num1,res))
                                        elif choice == 3:
                                                res = (num1 * num2)
                                                print("Product of {} and {} = {} \n==================================================================================================".format(num1,num2,res))
                                        elif choice == 4:
                                                res = (num1 / num2)
                                                print("{} Divided by {} = {} \n==================================================================================================".format(num1,num2,res))

                        elif choice == 5:
                                print("To calculate with the result of previous calculation, Just enter res in the field of number.\nEg: Consider the value of result as 49 and the choice as Square Root for the sake of this example.\n√res\nResult= 7\nEnter Two Numbers: ")
                                root = input("√")
                                if (root == "res"):
                                        root = float(res)
                                        res = root ** 0.5
                                        print("√{} = {} \n==================================================================================================".format(root,res))
                                else:
                                        root = float(root)
                                        res = root ** 0.5
                                        print("√{} = {} \n==================================================================================================".format(root,res))

                        else:
                                banner("Exiting")
                                exit()
        else:
                while True:
                        print("\n1.Addition")
                        print("2.Subtraction")
                        print("3.Multiplication")
                        print("4.Division")
                        print("5.Square Root")
                        print("6.Exit")

                        choice = int(input("Enter Your Choice: "))
                        print("==================================================================================================")
                        if (choice >= 1 and choice <= 4):
                                values = int(input("How many values do you want to calculate? \n"))
                                if choice == 1:
                                        for i in range(values):
                                                numbers.append(float(input()))
                                        print("Result = "+str(sum(numbers))+"\n==================================================================================================")

                                elif choice == 2:
                                        for i in range(values):
                                                numbers.append(float(input()))
                                                subtr = reduce(operator.sub, numbers)
                                        print("Result = "+str(subtr)+"\n==================================================================================================")

                        elif choice == 5:
                                root = float(input("√"))
                                rootres = root ** 0.5
                                print("√{} = {} \n==================================================================================================".format(root,rootres))

                        else:
                                banner("Exiting")
                                exit()
else:
        print("Invalid Input!\nExiting....")
			
					
				
