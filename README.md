# Instructions for Using the BMI Calculator Program

To run the program, type in "python BMICalculator.py" or "python3 BMICalculator.py" (if version 3 needs to be specified) into the Terminal or GitBash window.

## Interface

When the program is run, the following is printed:

```
Welcome to the BMI Calculator!
Options:
1 - BMI Check
9 - Quit
Enter your choice:
```

To proceed, the user can enter '1' to access the BMI calculator; otherwise, the user can enter '9' to exit the program.

## BMI Data Entry (Weight & Height)

If the former is chosen, the user is prompted to input a weight either in kilograms or pounds. As mentioned in the prompt, the user should be entering the weight in a specified format (eg. XX lb or XX kg):

```
Enter your weight in kg/lb (eg. 130 lb):
```

After the weight is entered, the user is then prompted to input a height either in meters or inches. The format is similar to that for weight:

```
Enter your height in m/in (eg. 65 in):
```

## BMI Calculation and Output

After these two values are entered, the program automatically calculates the value of the BMI index as well as the associated category (shown below).

Underweight:    BMI < 18.5 <br/>
Normal weight:  18.5 <= BMI < 25 <br/>
Overweight:     25 <= BMI < 30 <br/>
Obese:          30 < BMI <br/>

The results are then printed along with the entered weight and height, an example of which is shown below:

```
The entered weight is 125 lb
The entered height is 63 in
The calculated BMI is 22.142466726102995
The result is normal weight
```
