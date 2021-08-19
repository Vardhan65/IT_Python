#Write a program - covert a percentage to a fraction 


import fractions


def percent_to_fraction(percent_number):
    decimal_number = percent_number / 100
    fraction = fractions.Fraction(decimal_number)
    return fraction


percent_input = 30
fraction_output = percent_to_fraction(percent_input)
print('fraction result is:{0}'.format(fraction_output))