def BMI_Calculator(weight,height):
    value = weight/(height*height)
    if value < 18.5:
        result = "underweight"
    elif 18.5 <= value < 25:
        result = "normal weight"
    elif 25 <= value < 30:
        result = "overweight"
    else:
        result = "obese"
    return value, result

def BMI_DataEntry():
    w_input = input("\nEnter your weight in kg/lb (eg. 130 lb): ")
    w_data = w_input.split(" ")
    h_input = input("Enter your height in m/in (eg. 65 in): ")
    h_data = h_input.split(" ")

    if len(w_data) != 2 or len(h_data) != 2:
        print("Please give an appropriate input.\n")
        return
    if w_data[1] not in ["lb","kg"] or h_data[1] not in ["in","m"]:
        print("Please give an appropriate input.\n")
        return
    if w_data[1] == "lb":
        try:
            weight = float(w_data[0])/2.20462 #convert lb to kg
        except ValueError:
             print("Please give an appropriate input.\n")
             return
    else:
        try:
            weight = float(w_data[0])
        except ValueError:
             print("Please give an appropriate input.\n")
             return
    if h_data[1] == "in":
        try:
            height = float(h_data[0])/39.37 #convert in to m
        except ValueError:
             print("Please give an appropriate input.\n")
             return
    else:
        try:
            height = float(h_data[0])
        except ValueError:
             print("Please give an appropriate input.\n")
             return
             
    value, result = BMI_Calculator(weight,height)
    print("\nThe entered weight is {} {}".format(w_data[0], w_data[1]))
    print("The entered height is {} {}".format(h_data[0], h_data[1]))
    print("The calculated BMI is {}".format(value))
    print("The result is {}\n".format(result))

def interface():
        print("Welcome to the BMI Calculator!")
        keep_running = True
        while keep_running:
            print("Options: ")
            print("1 - BMI Check")
            print("9 - Quit")
            choice = input("Enter your choice: ")
            if choice == '9':
                keep_running = False
            elif choice == '1':
                BMI_DataEntry()
            else:
                print("\nPlease select one of the options.\n")
        return

if __name__ == "__main__":
        interface()
