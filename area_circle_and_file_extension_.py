'''

MyCaptain assignment 1
author : Akshay kalyan
date : 26-02-2022

'''

#1. printing the area of circle by taking radius as and input from user

from cmath import pi

radius=float(input("Input the radius of the circle: "))
print(f"area of the circle {radius} is: \n", radius*radius*pi)

#-------------------------------------------------------------------------------------------------------------------------------

#2. program to print the file extension after acceptng the filename from user

filename=input("enter the full name of file: ")
file_and_ext=filename.split(".")
if file_and_ext[1] == "py":
    print("the extension of the file is python")
    
