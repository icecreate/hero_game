while True:
    x=int(input('x:'))
    y=int(input('y:'))
    o=input('operator:')
    operator={
        '+':x+y,
        '-':x-y,
        '*':x*y,
        '/':x/y
    }
    result=operator.get(o,'Please input the correct operator,such as + - * /')
    print(result)