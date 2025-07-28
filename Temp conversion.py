while True:
    num = int(input("Enter conversion type➣ (1) Celcius ➜ farenheit (2) Farenheit ➜ celcius (0)➜quit: "))
    if num == 0:
        print("Ok, exiting...")
        break
    try:
        if num == 1:
            sol = float(input("Enter a temperature(in xC only!): "))
            ans = (sol*(9/5)+32)
            print(f"{sol}C in farenheit is: {ans}F")

        elif num == 2:
            sol = float(input("Enter a temperature(in xF only!): "))
            ans = ((sol-32)*5/9)
            print(f"{sol}F in celcius is: {ans}C")

    except ValueError:
        print("Invalid Temperature entered!")

        
              
