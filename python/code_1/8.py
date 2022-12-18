#find the rest angle value of the triangle

angle1 = float(input("Enter the angle 1 : "))
angle2 = float(input("Enter the angle 2 : "))

if (angle1 + angle2) > 180:
    print("This can't be a triangle !")
elif (angle1 + angle2) == 180:
    print("This is not a triangle, this is a line")
else:
    angle3 = 180 - (angle1+angle2)
    print("Angle 3 : " , angle3)