has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:     #AND condition is for both conditions to be true
    print("Eligible for loan")

if has_high_income or has_good_credit:      #OR condition is for either condition to be true
    print("Eligible for loan")    

if has_high_income and not has_criminal_record:  #NOT condition is for the opposite of the condition to be true
    print("Eligible for loan")