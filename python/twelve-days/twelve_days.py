carrol_data = {
    0:['first','a Partridge in a Pear Tree'],
    1:['second', 'two Turtle Doves'],
    2:['third', 'three French Hens'],
    3:['fourth', 'four Calling Birds'],
    4:['fifth', 'five Gold Rings'],
    5:['sixth', 'six Geese-a-Laying'],
    6:['seventh', 'seven Swan-a-Swimming'],
    7:['eighth', 'eight Maids-a-Milking'],
    8:['nineth', 'nine Ladies Dancing'],
    9:['tenth', 'ten Lords-a-Leaping'],
    10:['eleventh', 'eleven Pipers Piping'],
    11:['twelfth', 'twelve Drummers Drumming'],
}
def recite(start_verse, end_verse):
    if start_verse > end_verse:
        raise ValueError('End verse needs to be equal or greater than start verse')
    if start_verse > 12 or end_verse > 12 or start_verse < 1 or end_verse < 0:
        raise ValueError('Start and end verse need to be gratear than 0 and smaller than 13')
    
    current_verse = start_verse
    result = []

    while current_verse <= end_verse:
        result.append("On the {} day of Christmas my true love gave to me: {}.".format(carrol_data[current_verse - 1][0], carrol_data[current_verse - 1][1]))
        current_verse += 1
    
    return result

# On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
# On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
# On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.