#!/bin/python3
from functools import reduce
import operator
from pyfiglet import Figlet

def banner(text):
	custom_fig = Figlet(font='graffiti')
	print(custom_fig.renderText(text))

banner("Calculator")
print("								V1.0")
print("								Coded by : Vu1n3rab1e")
numbers = []

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
			print("5.Exit")

			choice = int(input("Enter Your Choice: "))
			print("==================================================================================================")
			if (choice >=1 and choice <=4):
				print("Enter Two Numbers: ")
				num1 = int(input())
				num2 = int(input())
				if choice == 1:
					res = num1 + num2
					print("Sum of {} and {} = {}.\n==================================================================================================".format(num1,num2,res))
				elif choice == 2:
					res = num1 - num2
					print("Difference of {} and {} = {}.\n==================================================================================================".format(num2,num1,res))
				elif choice == 3:
					res = num1 * num2
					print("Product of {} and {} = \n==================================================================================================".format(num1,num2,res))
				elif choice == 4:
					res = num1 / num2
					print("{} Divided by {} = \n==================================================================================================".format(num1,num2,res))
								
			else:
				banner("Exiting")
				exit()	
	else:
		while True:
			print("\n1.Addition")
			print("2.Subtraction")
			print("3.Multiplication")
			print("4.Division")
			print("5.Exit")
		
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
			else:
				banner("Exiting")
				exit()
else:
	print("Invalid Input!\nExiting....")		
				
