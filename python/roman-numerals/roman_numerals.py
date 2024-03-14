def roman(num):
    arabic_to_roman_map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    
    roman_numeral = ''
    for arabic, roman in arabic_to_roman_map.items():
        while num >= arabic:
            roman_numeral += roman
            num -= arabic
    return roman_numeral
