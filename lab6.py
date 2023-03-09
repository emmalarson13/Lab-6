#Emma Larson

def encoder__(data):
    variable=1
    result=0
    while data >0:
        digit= data %10 +3
        result +=digit * variable
        variable*=10
        data=data//10
    return result




#start of function:

while True:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    option= int(input('Please enter an option: '))
    if option==1:
        temp= encoder__(int(input('Please enter your password to encode: ')))
        print('Your password has been encoded and stored! ')
    if option == 2:

        print(f"The encoded password is {temp}, and the original password is {decoder__(temp)}.")
        print(decoder__(temp))
    if option==3:
        break

