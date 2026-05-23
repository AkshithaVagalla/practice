course = "Python for Beginners"
len = len(course) #len() is a built-in function that returns the length of a string
print(len)
course.capitalize()
print(course.capitalize()) #capitalizes the first letter of the string
print(course.upper()) #converts the string to uppercase
print(course.lower()) #converts the string to lowercase
print(course.find('P')) #returns the index of the first occurrence of the character 'P' in the string, which is 0
print(course.find('p')) #returns -1 because 'p' is not found in the string (case-sensitive)
print(course.replace('Beginners', 'Absolute Beginners')) #replaces the word 'Beginners

'python' in course #returns True if the word 'python' is found in the string, otherwise returns False (case-sensitive)
print('python' in course) #returns False because 'python' is not found in the

course.title() #converts the first letter of each word to uppercase
print(course.title())