"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat_no = 1
    while number >= seat_no:
        if seat_no % 4 == 1:
            yield "A"
        elif seat_no % 4 == 2:
            yield "B"
        elif seat_no % 4 == 3:
            yield "C"
        elif seat_no % 4 == 0:
            yield "D"
        seat_no = seat_no + 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_no = 1
    seat_letter = generate_seat_letters(number)
    while number >= seat_no:
        row_no = int(seat_no / 4 - 0.1) + 1
        if row_no < 13:
            yield str(row_no) + next(seat_letter)
        else:
            yield str(row_no + 1 ) + next(seat_letter)
        seat_no += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    result = {}
    seat = generate_seats(len(passengers))
    for passenger in passengers:
        result[passenger] = next(seat)
    return result


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    code = ''
    for seat_number in seat_numbers:
        code = str(seat_number) + str(flight_id)
        while len(code) < 12:
            code = code + '0'
        yield code
