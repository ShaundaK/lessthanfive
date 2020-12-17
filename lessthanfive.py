#take a list and print out the elements of the list less than 5
#so print out 1, 1, 2, 3

#then make a new list that has all of the elements less than 5 and print it out
#write in one line of python..

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

count = 0
for number in a: #"in" iterates through the word "banana"
    if number < 5:
        print(number)

b = [1, 1, 2, 3]
print(*b)
