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
    if w_data[1] == "lb":
        weight = float(w_data[0])/2.20462 #convert lb to kg
    else:
        weight = float(w_data[0])
    h_input = input("Enter your height in m/in (eg. 65 in): ")
    h_data = h_input.split(" ")
    if h_data[1] == "in":
        height = float(h_data[0])/39.37 #convert in to m
    else:
        height = float(h_data[0])
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
