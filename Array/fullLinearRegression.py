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




model_choice = input("Which model to run (linear, ridge, logistic or Lasso)? ").lower().strip()

if model_choice == 'linear':
    print(" here we are doing for linear regression")

elif model_choice =='ridge':
    print("Here you are doing for rigid regression")

    print("now you are doing with Lasso")
else:
    print("Invalid input please re-try to select proper input")

