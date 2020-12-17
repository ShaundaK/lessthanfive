#take a list and print out the elements of the list less than 5
#so print out 1, 1, 2, 3

#then make a new list that has all of the elements less than 5 and print it out
#write in one line of python..

#then ask user for a number and return a list that contains only elements from the original list that are smaller than the number given by the user

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
count = 0
user = input("Enter a number.  ")
user_input = int(user)

#def smaller_numbers(number):
for number in a: #"in" iterates through the word "banana"
    if number < user_input:
        count = count + 1
        print(number)

#b = [1, 1, 2, 3]
#print(*b)
