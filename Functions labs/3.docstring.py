def readable_timedelta(days):
    # insert your docstring here
    # This Function Converts Number of Days and Weeks
    # The Variable (Weeks) returns How may weeks are the number of days

    # The Variable (days) returns the remaining days
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)