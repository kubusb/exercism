"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number +1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
    
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    card_av_sum = 0
    for item in hand:
        card_av_sum = card_av_sum + item
    
    return card_av_sum / len(hand)


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    av_first_last = (hand[0] + hand[-1]) / 2

    av_fl_card = bool(av_first_last == card_average(hand))
    
    median = len(hand) // 2
    
    av_med_card = bool(hand[median] == card_average(hand))
    
    if ((av_fl_card or av_med_card) is True) or ((av_fl_card and av_med_card) is True):
        return True
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd_cards_list = hand[0::2]
    print(str(odd_cards_list))
    
    sum_of_odd_cards = 0
    for card in odd_cards_list:
        sum_of_odd_cards = sum_of_odd_cards + card 
    
    avarage_of_odd_cards = sum_of_odd_cards / len(odd_cards_list)
    
    even_cards_list = hand[1::2]
    
    sum_of_even_cards = 0
    for card in even_cards_list:
        sum_of_even_cards = sum_of_even_cards + card
    
    avarage_of_even_cards = sum_of_even_cards / len(even_cards_list)
    
    return bool(avarage_of_odd_cards == avarage_of_even_cards)
    


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    return hand 
