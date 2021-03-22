
def num_translate(number):

    dictionary_of_numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
                            'eight ': 'восемь', 'nine': 'девять', 'ten': 'десять', 'eleven': 'одинадцать', 'twelve': 'двенадцать',
                            'thirteen': 'тринадцать', 'fourteen': 'четырнадцать', 'fifteen': 'пятнадцать', 'sixteen': 'шестнадцать',
                            'eighteen': 'восемнадцать', 'nineteen': 'девятнадцать', 'twenty': 'двадцать'
                             }
    if number.istitle() and dictionary_of_numbers.get(number) != None:
        print(dictionary_of_numbers[number.lower()].capitalize())
    elif not number.istitle() and dictionary_of_numbers.get(number) != None:
        print(dictionary_of_numbers[number])
    else:
        print(dictionary_of_numbers.get(number))


num_translate('one')
num_translate('Two')
num_translate('nine')
num_translate('Nine')
num_translate('nNine')
num_translate('Zero')
num_translate('zero')
num_translate('twenty five')
num_translate('Twenty five')