# Escreva um programa que converta uma temperatura digitada em °C e converta para °F
grausC = float(input('Digite sua temperatura atual em °C: '))
Celsius = ((grausC - 32) * 5) / 9 # Esta conta mostrará o valor em Celsius
Fahrenheit = ((grausC * 9) / 5) + 32 # Esta conta mostrará o valor em Fahrenheit
Kelvin = grausC + 273.15
print('Sua temperatura em °C (Celsius) de {}, mostrada em Fahrenheit (°F) e Kelvin (°K) resulta em:\n°F: {:^8}\n°K:{:^8}'.format(grausC,Fahrenheit,Kelvin))