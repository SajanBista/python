# code to collect data:
datas =[]

while True:
    a = input("how many datas do you have?\n ")

    try:
        num_data = int(a)
        break
    except ValueError:
        print(" please enter the correct value.")

try:
    num_data = int(a) #making all the datas numeric

    print("for collecting datas")
    for i in range(num_data):
        data_point_str =  input(f"Enter data point #{i+1}:")
        data_point_float = float(data_point_str)
        datas.append(data_point_float)

    print(f"successfully collected datas and the list that you entered is {datas}")


except ValueError:
    print("invalid input so please retry")

model_choice = input("Which model to run (linear, ridge, logistic or Lasso)? ").lower().strip()

if model_choice == 'linear':
    print(" here we are doing for linear regression")

elif model_choice =='ridge':
    print("Here you are doing for rigid regression")
elif model_choice == 'logistic':
    print(" here you are doing with logistic regression")
elif model_choice =='Lasso':
    print("now you are doing with Lasso")
else:
    print("Invalid input please re-try to select proper input")

