from datetime import date, timedelta
from calendar import monthrange

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date."""
    def __init__(self, message="That day does not exist."):
        self.message = message
        super().__init__(self.message)

def meetup(year, month, week, day_of_week):
    # Dictionary to map day names to weekday numbers (0-6)
    days = {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
        'Friday': 4, 'Saturday': 5, 'Sunday': 6
    }
    
    # Get the first day of the month and the number of days in the month
    first_day = date(year, month, 1)
    _, last_day = monthrange(year, month)
    
    # Find the first occurrence of the day in the month
    first_occurrence = first_day + timedelta((days[day_of_week] - first_day.weekday() + 7) % 7)
    
    if week == 'teenth':
        # Find the teenth occurrence
        while first_occurrence.day < 13:
            first_occurrence += timedelta(days=7)
    elif week in ['first', 'second', 'third', 'fourth', 'fifth']:
        # Find the nth occurrence
        n = ['first', 'second', 'third', 'fourth', 'fifth'].index(week)
        first_occurrence += timedelta(days=7 * n)
        if first_occurrence.month != month:
            raise MeetupDayException()
    elif week == 'last':
        # Find the last occurrence
        while (first_occurrence + timedelta(days=7)).month == month:
            first_occurrence += timedelta(days=7)
    else:
        raise ValueError("Invalid week specifier")
    
    if first_occurrence.month != month:
        raise MeetupDayException()
    
    return first_occurrence
