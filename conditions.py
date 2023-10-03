#CS104
#Christopher DeTullio
#conditions.py
i = 1
while i <= 5:
    y = True
    temp = int(input("Please enter the current temperature: "))
    if temp > 90:
        print("Wear Shorts")
    elif temp > 70:
        print("Short sleeves are fine")
    elif temp > 50:
        print("Wear a jacket")
    elif temp > 32:
        print("Wear a heavy coat")
    else:
        print("Stay Inside")

    while y:
        x = str(input("Would you like to enter another temperature? "))  
        if x == "yes":
            print("Restarting...")
            y = False
        elif x == "no":
            print("Goodbye!")
            i = 6
            y = False
        else:
            print("Please enter either yes or no. ")
    i += 1
if i > 6:
    print("Have a nice day!")
    
