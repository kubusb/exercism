class Clock:
    def __init__(self, hour, minute):
        self.total_minutes = (hour * 60 + minute) % (24 * 60)

    def __repr__(self):
        hours, minutes = divmod(self.total_minutes, 60)
        return f"Clock({hours}, {minutes})"

    def __str__(self):
        hours, minutes = divmod(self.total_minutes, 60)
        return f"{hours:02}:{minutes:02}"

    def __eq__(self, other):
        return self.total_minutes == other.total_minutes

    def __add__(self, minutes):
        return Clock(0, self.total_minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.total_minutes - minutes)
