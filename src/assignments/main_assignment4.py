from src.assignments.assignment4 import factorial

def main():#void function
    '''
    Create a loop that'll run until the user doesn't type the letter 'y'
    In the loop,
    Capture one number from the keyboard and validate for a range between 1 and 10.
    Call the factorial function.
    Save the result to a variable.
    Print the variable value.

    Ask the user if they want to continue.

    TO RUN YOUR PROGRAM GO TO IN PYTHON IDLE RUN->RUN MODULE.
    IN THE PYTHON SHELL TYPE main()

    DON'T ADD A RETURN STATEMENT TO THIS FUNCTION
    '''
    try_again = 'y'
    while try_again == 'y':
        user = int(input('Enter a number: '))
        while user < 1 or user > 10:
            print ('Value must be between 1-10.')
            user = int(input('Enter a number: '))
        result = factorial(user)
        print (result)
        try_again = str(input('Type y to continue... '))
main()


#another option to run the program is to call the main() function below and Run->Run Module
