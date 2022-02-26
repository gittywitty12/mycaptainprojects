from cmath import pi


radius=float(input("Input the radius of the circle: "))
print(f"area of the circle {radius} is: \n", radius*radius*pi)


filename=input("enter the full name of file: ")
file_and_ext=filename.split(".")
if file_and_ext[1] == "py":
    print("the extension of the file is python")




