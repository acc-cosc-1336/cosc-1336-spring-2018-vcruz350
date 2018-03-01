#write import statements for homework 6 functions
from src.homework.homework6 import get_point_mutations
from src.homework.homework6 import get_dna_complement
from src.homework.homework6 import transcribe_dna_into_rna
from src.homework.homework6 import get_gc_content

def menu_options():
    print()
    print('1) Point Mutations')
    print('2) DNA Complement')
    print('3) DNA to RNA')
    print('4) GC Content')
    print('5) DNA motif')
    print('6) Most likely Ancestor')
    print('7) Exit')
    print()

def run_menu():

    option = -1

    while option != 7:
        menu_options()
        option = int(input("Enter menu choice: "))

        while option < 1 or option > 7:
            print("Valid menu range 1-7")
            option = int(input("Enter menu choice: "))

        if option == 1:
            handle_option_1()
        elif option == 2:
            handle_option_2()
        elif option == 3:
            handle_option_3()
        elif option == 4:
            handle_option_4()
        elif option == 5:
            handle_option_5()
        elif option == 6:
            handle_option_6()


def handle_option_1():
    '''
    Write code to:
    Loop as long as user wants to continue.
    Prompt user for two dna strings of length 10 with letter range A,C,G, and T only.  
    Call the function get_point_mutations and display the mutations to screen.
    Ask user if they want to continue.
    '''
    
    keep_going = 'y'
    while keep_going == 'y':
        dna_string1 = input('Enter first 10 digit DNA code using letters A, C, G and T: ')

        while len(dna_string1) != 10:
            dna_string1 = input('Enter first 10 digit DNA code using letters A, C, G and T: ')

        dna_string2 = input('Enter second 10 digit DNA code using the same letter options: ')

        while len(dna_string2) != 10:
            dna_string2 = input('Enter second 10 digit DNA code using the same letter options: ')

        result = get_point_mutations(dna_string1, dna_string2)
        print(result)
        keep_going = input('Enter y to continue... ')

def handle_option_2():
    '''
    Write code to read the file dna_complement.dat.
    For each line string call the function get_dna_complment and display the complement to screen.
    '''
    
    read_file = open('dna_complement.dat', 'r')

    for line in read_file:
        line = line.rstrip('/n')
        print(get_dna_complement(line))

    read_file.close()

def handle_option_3():
    '''
    Write the code to read the file transcribe_dna_to_rna.dat.
    For each line string call the function transcribe_dna_to_rna and display rna to screen.
    '''
    
    read_file = open('transcribe_dna_to_rna.dat', 'r')

    for line in read_file:
        line = line.rstrip('/n')
        print(transcribe_dna_into_rna(line))

    read_file.close()
    
def handle_option_4():
    '''
    Write code to read the file compute_gc_content.dat and for each line
    call the get_gc_content function with the line string as an argument.
    Display the gc_content for each line.
    '''
    
    read_file = open('compute_gc_content.dat', 'r')

    for line in read_file:
        line = line.rstrip('/n')
        print(get_gc_content(line))

    read_file.close()
    
def handle_option_5():
    pass #optional 

def handle_option_6():
    pass #optional
