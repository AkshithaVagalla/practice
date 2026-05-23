first_name = "john"
last_name = "smith"
message = first_name + " [ " + last_name + " ] " "is a coder"  #not ideal , too complicated and hard to read
print(message)

# better way to format strings is using f-strings
first_name = "john"
last_name = "smith"     
msg = f'{first_name} [{last_name}] is a coder'  # f stands for formatted string, we can use curly braces to insert variables into the string,

# curly braces are used because they are not used in normal string concatenation, so it is easier to read and understand the code.
print(msg)