def check_palindrome_1(string):
    reversed_string = string[::-1]
    status = True
    if (string != reversed_string):
        status = False
    return status


string = input("Enter the string: ")
status = check_palindrome_1(string)
if (status):
    print("It is a palindrome ")
else:
   print("Sorry! Try again")
