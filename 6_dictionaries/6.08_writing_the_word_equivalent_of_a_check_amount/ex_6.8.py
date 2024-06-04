""" Prgoram that writes the word equivalent of a check amount """
# ~~~~~~~~~  Definition of Functions  ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
# dictionaries for number to word conversion
units = {
    0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE',
    6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'
}

teens = {
    10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 14: 'FOURTEEN',
    15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN', 18: 'EIGHTEEN', 19: 'NINETEEN'
}

tens = {
    2: 'TWENTY', 3: 'THIRTY', 4: 'FOURTY', 5: 'FIVETY', 6: 'SIXTY',
    7: 'SEVENTY', 8: 'EIGHTY', 9: 'NINETY'
}

def convert_to_words( number ):
    if number<10:
        return units[number]
    elif number<20:
        return teens[number]
    elif number<100:
        ten, one = divmod(number, 10)
        return tens[ten] + (' ' + units[one] if one!=0 else '')
    else:
        hundred, remainder = divmod(number, 100)
        return units[hundred] + (' HUNDRED ' + convert_to_words(remainder) if remainder!=0 else '')
# end convert_to_words

def convert_check_amount( amount ):
    dollars, cents = divmod(int(amount*100), 100)
    dollars_words = convert_to_words( dollars )
    return f"{dollars_words} AND {cents:02} /100"
# end convert_check_amount

# ~~~~~~~~~  Program Execution     ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
check_amount = 628.83
check_amount1 = 999.99
check_amount2 = 290.48
words = convert_check_amount( check_amount )
words1 = convert_check_amount( check_amount1 )
words2 = convert_check_amount( check_amount2 )

print(words, end="\n\n")
print(words1, end="\n\n")
print(words2)
