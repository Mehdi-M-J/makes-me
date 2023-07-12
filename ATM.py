Balance = 0

while True:
    print('1.mojoodi')
    print('2.varizi')
    print('3.bardasht')
    print('4.exit')
    id = input('Enter the NUMBER>>>')
    if id == "1":
        print(f'balance : {Balance}')
    elif id == "2":
        pool = int(input('please enter the pool>>>'))
        Balance += pool
        print(f'balance : {Balance}')
    elif id == "3":
        pool = int(input('please enter the pool>>>'))
        if pool > Balance:
            print('mojoodi shoma kafi nist😭😭')
        else:
            Balance -= pool
            print(f'balance : {Balance}')
    elif id == "4":
        print('good bey👋')
        break
    else:
        print('vorodi eshtebah ast')