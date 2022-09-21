import unittest
def convert_decimal_to_roman(decimal_number):

    roman = ''
    valor_mil=''
    valor_cen=''
    valor_dec=''
    valor_uni=''
    mil= (decimal_number // 1000)
    cen= (decimal_number // 100)
    dec= (decimal_number // 10)
    uni= (decimal_number % 10)

    if mil>0 and mil<4:
        valor_mil += 'M'*(mil)

    if cen>0 and cen<4:
        valor_cen += 'C'*(cen)
    if cen== 4:
        valor_cen = 'CD'
    if cen== 5:
        valor_cen = 'D'
    if cen>5 and cen<9:
        resto= cen-5
        valor_cen = 'D' + 'C'*(resto)
    if cen== 9:
        valor_cen = 'CM'    
    if dec>0 and dec<4:
        valor_dec += 'X'*(dec)
    if dec== 4:
        valor_dec = 'IL'
    if dec== 5:
        valor_dec = 'L'
    if dec>5 and dec<9:
        resto= dec-5
        valor_dec = 'L' + 'X'*(resto)
    if dec== 9:
        valor_dec = 'XC'    
    if uni>0 and uni<4:
        valor_uni += 'I'*(uni)
    if uni== 4:
        valor_uni = 'IV'
    if uni== 5:
        valor_uni = 'V'
    if uni>5 and uni<9:
        resto= uni-5
        valor_uni += 'V' + 'I'*(resto)
    if uni== 9:
        valor_uni += 'IX'    
    
    roman = valor_mil + valor_cen + valor_dec + valor_uni

    return roman
class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        roman_number = convert_decimal_to_roman (1111)
        self.assertEqual(roman_number, 'MCXI')
    
        #Porque falla cuando combino mil, centena y decena

if __name__ == '__main__': unittest.main()