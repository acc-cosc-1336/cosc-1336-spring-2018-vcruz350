def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''
    
    #set staring variables to 0
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0

    #count number of A's
    for ch1 in dna_string:
        if ch1 == 'A' or ch1 == 'a':
            count_A += 1

    #count number of C's
    for ch2 in dna_string:
        if ch2 =='C' or ch2 == 'c':
            count_C += 1

    #count number of G's
    for ch3 in dna_string:
        if ch3 == 'G' or ch3 == 'g':
            count_G += 1

    #count number of T's
    for ch4 in dna_string:
        if ch4 == 'T' or ch4 == 't':
            count_T += 1
            
    return count_A, count_C, count_G, count_T

    
