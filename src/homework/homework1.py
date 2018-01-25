#calculate hours, minutes and seconds

def get_hours_since_midnight(seconds):
    total_hours = seconds // 3600
    '''
    Type the code to calculate total hours given n(number) of seconds
    For example, given 3800 seconds the total hours is 1
    '''
    return total_hours

'''
IF YOU ARE OK WITH A GRADE OF 70 FOR THIS ASSIGNMENT STOP HERE.
'''

def get_minutes(seconds):
    remaining_seconds = seconds % 3600
    total_minutes = remaining_seconds // 60
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 3
    '''

    return total_minutes

def get_seconds(seconds):
    remaining_seconds = seconds % 3600
    total_minutes = remaining_seconds // 60
    total_seconds = total_minutes % 60
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 20
    '''

    return total_seconds
