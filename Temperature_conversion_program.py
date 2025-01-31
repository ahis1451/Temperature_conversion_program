# Temperature Conversion program
degree_symbol = '\u00b0'
print('Convert your temperature reading from celsius to fahrenheit or fahrenheit to celsius FOR FREE!!!')
temp = float(input('Enter the temperature reading you want to convert: '))
unit = input('is that in fahrenheit or celsius? (please type F or C): ')

if unit == "C":
    temp = round((9 * temp) / 5 + 32,1)
    print(f'the temperature in fahrenheit is equal to {temp}{degree_symbol}F')
elif unit == "F":
    temp = round((temp - 32) * 5 / 9,1)
    print(f'the temperature in celsius is equal to {temp}{degree_symbol}C')
else:
    print(f'{unit} is not a valid unit of measurement, please enter F or C CAPITALIZED')