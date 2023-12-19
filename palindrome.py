# exercise for palindrom identification
# palindrome is a word that reads the same way from left to right and vice versa.

# method for recognition if the string is palindrome or not
def is_palindrome(given_string):
    clear_string = given_string.lower().replace(" ", "")
    return clear_string == clear_string[::-1]


# place of usage
input_string = input("Write the word you want to know if it's palindrome or not:")
print(is_palindrome(input_string))
