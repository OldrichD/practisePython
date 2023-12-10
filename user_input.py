
# exercise for use of input and validation of it

# validation if the input is name in correct form
def name_validation(string):
    return string is not None and string[0].isupper() and string.isalpha()


# validation if the age is integer in <0,120>
def age_validation(integer):
    try:
        age = int(integer)
        return 0 <= age <= 120
    except ValueError:
        return False


# user input his name
user_name = input("Write your name:")

# loop for validation correct form of name and in case it is not, repeat the user input
while not name_validation(user_name):
    user_name = input("Write your name in correct form:")

# after success validation print sentence with name of user
print(f'Hi, your name is: {user_name}!')


# user input his age
user_age = input("Write your age:")

# loop for validation correct age and in case it is not, repeat the user input
while not age_validation(user_age):
    user_age = input("Write your age like whole number from 0 to 120:")

# after success validation print sentence with name of user
print(f'{user_name}, your age is: {user_age}!')
