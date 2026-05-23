course = "Python's for Beginners" #double quotes can be used to avoid syntax error when string contains single quote
print(course)

course = 'python for "Beginners"'
print(course)



course = '''
This is a multi line string. 
We can write as much as we want.'''
print(course)



course = "Python's for Beginners"
print(course[0]) #prints the first character of the string
print(course[-1]) #prints the last character of the string  

print(course[0:3]) #prints characters from index 0 to 2 (3 is exclusive)

print(course[0:]) #prints the whole string from index 0 to the end
print(course[1:]) #prints the whole string from index 1 to the end
print(course[:5]) #prints the first 5 characters of the string (index 0 to 4)