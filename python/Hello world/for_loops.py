#for loops are used in simple words to repeat a block of code a certain number of times.

#loop variable in simple words is used to store the current value of the loop, it is also called the loop counter, it is used to keep track of the number of iterations of the loop.




for item in "python": # this will iterate over each character in the string "python" and assign it to the variable item, so in the first iteration, item will be 'p', in the second iteration, item will be 'y', and so on.
    print(item)

for item in ["john", "sarah", "michael"]: # this will iterate over each item in the list and assign it to the variable item, so in the first iteration, item will be 'john', in the second iteration, item will be 'sarah', and so on.
    print(item)

#range in simple words is a built-in function that generates a sequence of numbers, it takes three arguments, start, stop, and step, start is the number to start the sequence from, stop is the number to end the sequence at (not inclusive), and step is the number to increment the sequence by (default is 1).
for item in range(10): # this will iterate over the numbers from 0 to 9 and assign it to the variable item, so in the first iteration, item will be 0, in the second iteration, item will be 1, and so on.
    print(item)

for item in range(5, 10): # this will iterate over the numbers from 5 to 9 and assign it to the variable item, so in the first iteration, item will be 5, in the second iteration, item will be 6, and so on.
    print(item)

for item in range(0, 10, 2): # this will iterate over the numbers from 0 to 9 with a step of 2 and assign it to the variable item, so in the first iteration, item will be 0, in the second iteration, item will be 2, and so on.
    print(item)