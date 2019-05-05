#demos string methods
def main():
    #get string from user
    user_string = input('Enter a string: ')
    
    print('This is what I know about the string:')

    #Test the string
    if user_string.isalnum():
        print('This string is alphanumeric')
    if user_string.isdigit():
        print('This string contains only digits')
    if user_string.isalpha():
        print('This string contains only alphabetic characters')
    if user_string.isspace():
        print('This string contains only whitespace characters')
    if user_string.islower():
        print('The letters in the string are all lowercase')
    if user_string.isupper():
        print('The letters in the string are all uppercase')

main()