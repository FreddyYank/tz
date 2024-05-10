from art import tprint


tprint("CALC v1.0")

a = float(input('Первое число:'))
c = input('Выбери знак(+,-,*,/,%):')
b = float(input('Второе число:'))

if c == '+':
    d = a+b
    print("{} {} {} = {}".format(a,c,b,d))
elif c == '-':
    d = a-b
    print("{} {} {} = {}".format(a,c,b,d))
elif c == '*':
    d = a*b
    print("{} {} {} = {}".format(a,c,b,d))
elif c == '/':
    d = a/b
    print("{} {} {} = {}".format(a,c,b,d))
elif c == '%':
    d = a%b
    print("{} {} {} = {}".format(a,c,b,d))
else:
    print('Ошибка')