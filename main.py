def get_even(number):
    if number % 2 == 0:
        return True
    return False


for i in range(1440):
    a = int(input('A'))
    print(get_even(a))