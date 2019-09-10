def BMI_DataEntry():
    w_input = input("\nEnter your weight in kg/lb (eg. 130 lb): ")
    w_data = w_input.split(" ")
    if w_data[1] == "lb":
        weight = float(w_data[0])/2.20462
    else:
        weight = float(w_data[0])
    h_input = input("Enter your height in m/in (eg. 65 in): ")
    h_data = h_input.split(" ")
    if h_data[1] == "in":
        height = float(h_data[0])/39.37
    else:
        height = float(h_data[0])
    print("\nThe entered weight is {} kg".format(weight))
    print("The entered height is {} m\n".format(height))

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
