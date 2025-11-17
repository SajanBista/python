# code to collect data:
X_data =[]
Y_data =[]

while True:
    a = input("how many data point that you have? make sure that you have more than two\n ").strip()

    try:
        num_data = int(a)
        if num_data>=2:
            break
        print("there must be atleast 2 datas for prediction. ")

    except ValueError:
        print(" please enter the correct value.i.e Integer")

for i in range(num_data):
    print(f"\n-- Observation #{i + 1} --")

    while True:
        try:
            x_val_str = input(f"Enter X value (Independent Variable) for point #{i + 1}: ").strip()
            x_val_float = float(x_val_str)
            X_data.append(x_val_float)
            break
        except ValueError:
            print(" Invalid input. Please enter a number for X.")
    while True:
        try:
            y_val_str = input(f"Enter Y value (Dependent Variable) for point #{i + 1}: ").strip()
            y_val_float = float(y_val_str)
            Y_data.append(y_val_float)
            break
        except ValueError:
            print(" Invalid input. Please enter a number for Y.")

print(f"X Data (Independent): {X_data}")
print(f"Y Data (Dependent):   {Y_data}")


if len(set(X_data))<2:
    print("critical error! invalid dataset \n All X values are identical. The regression slope cannot be calculated.\n you must insert the datas i.e. different like 5 and 10")
    exit()

model_choice = input("Which model to run (linear, ridge, logistic or Lasso)? ").lower().strip()

if model_choice == 'linear':
    print(" here we are doing for linear regression")

    X_sum = sum(X_data)
    Y_sum = sum(Y_data)

    n = num_data

    if n>0:
        X_mean = X_sum/n
    else:
        print("there is no input or no x")
    if n>0:
        Y_mean = Y_sum/n
    else:
        print("there is no y value might you didn't entered")

    print(f"Mean of x value: {X_mean}")
    print(f"Mean of y value: {Y_mean}")


    #for numenator part:
    numenator = 0.0

    for  x_i, y_i in zip(X_data, Y_data):
        x_deviation = x_i - X_mean


        y_deviation = y_i -Y_mean
        product_of_deviation = x_deviation * y_deviation

        numenator += product_of_deviation

    
    denomenator =0.0
    #for denomemator:
    for x_i in(X_data):
        x_deviation = x_i - X_mean

        denomenator += x_deviation

    print(f"the numenator is {numenator} and denomenator = {denomenator}")













elif model_choice =='ridge':
    print("Here you are doing for rigid regression")

    print("now you are doing with Lasso")
else:
    print("Invalid input please re-try to select proper input")

