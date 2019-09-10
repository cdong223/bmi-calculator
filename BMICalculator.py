def interface():
        print("Welcome to the BMI Calculator!")
        keep_running = True
        while keep_running:
            print("Options: ")
            print("1 - BMI Check")
            print("9 - Quit\n")
            choice = input("Enter your choice: ")
            if choice == '9':
                keep_running = False
            elif choice == '1':
                print("\nBMI Interface\n")
            else:
                print("\nPlease select one of the options.\n")
        return

if __name__ == "__main__":
        interface()
