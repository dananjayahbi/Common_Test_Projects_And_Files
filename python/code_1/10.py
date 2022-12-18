#hours/minutes to seconds

def myFunction(input,type):
    seconds = 0
    
    if type == "Hours" :
        seconds = input * 60 * 60
        return seconds
    elif type == "Minutes":
        seconds = input * 60
        return seconds
    else:
        print("something wrong !")
    
a = input("Enter H to hours or Enter M to minutes : ")
time = ""

if a == "H":
    time = "Hours"
elif a == "M":
    time = "Minutes"
    
b = int(input("Enter the time : "))

result = myFunction(b,time)

print(result)