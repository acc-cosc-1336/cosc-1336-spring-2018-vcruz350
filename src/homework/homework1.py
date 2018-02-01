#determine number of hours
def get_hours_since_midnight(seconds):
    total_hours = seconds // 3600
    return ('Hours:' , total_hours)

#determine number of minutes
def get_minutes(seconds):
    remaining_seconds = seconds % 3600
    total_minutes = remaining_seconds // 60
    return ('Minutes:' , total_minutes)

#determine number of seconds
def get_seconds(seconds):
    remaining_seconds = seconds % 3600
    total_minutes = remaining_seconds // 60
    total_seconds = remaining_seconds - total_minutes * 60 
    return ('Seconds:' , total_seconds)
