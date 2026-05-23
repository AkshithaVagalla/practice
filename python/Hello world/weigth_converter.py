weight_of_the_user = int(input("enter the weight: "))
unit_of_the_user = input("(L)bs or (K)g: ")
if unit_of_the_user.upper == "L":
    converted_weight = weight_of_the_user * 0.45
    print(f"the weight of the user in kg is {converted_weight} kilos")
else :
    converted_weight_kg = weight_of_the_user / 0.45
    print(f"the weight of the user in lbs is {converted_weight_kg} pounds")