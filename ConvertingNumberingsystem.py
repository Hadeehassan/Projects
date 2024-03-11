# Abdallah Kareem Abdallah Ahmed , 20230228
# Reyad Youssef Ebrahim Mansour , 20230143
# Hady Hassan Ahmed Mohamed , 20230454
def dec_oct(number):
    My_list = []
    while number != 0:
        Rem = number % 8
        number = number // 8
        My_list.append(Rem)
    New_list = My_list[::-1]
    for element in New_list:
        print(element, end='')


def is_binary(num):
    for digit in num:
        if digit not in '01':
            return False
    return True


def is_octal(num):
    for digit in num:
        if digit not in '01234567':
            return False
    return True


def is_hexadecimal(num):
    valid_hex_chars = set('0123456789ABCDEFabcdef')
    for digit in num:
        if digit not in valid_hex_chars:
            return False
    return True


def bin_hex(number):
    def bin_dec(number):
        sum = 0
        i = 0
        while number != 0:
            dig = number % 10
            sum = sum + dig * (2 ** i)
            number = number // 10
            i = i + 1
        return sum

    def dec_hex(number):
        hex_digits = "0123456789ABCDEF"
        hexadecimal = ""
        while number > 0:
            remainder = number % 16
            if remainder < 10:
                hexadecimal = str(remainder) + hexadecimal
            else:
                hexadecimal = hex_digits[remainder] + hexadecimal
            number //= 16
        print("Hexadecimal NUMBER:", hexadecimal)

    num_dec = bin_dec(number)
    dec_hex(num_dec)


def bin_oct(number):
    def bin_dec(number):
        sum = 0
        i = 0
        while number != 0:
            dig = number % 10
            sum = sum + dig * (2 ** i)
            number = number // 10
            i = i + 1
        return sum

    def dec_oct(number):
        My_list = []
        while number != 0:
            Rem = number % 8
            number = number // 8
            My_list.append(Rem)
        New_list = My_list[::-1]
        for element in New_list:
            print(element, end='')

    num_dec = bin_dec(number)
    dec_oct(num_dec)


def oct_bin(number):
    def oct_dec(number):
        sum = 0
        i = 0
        while number != 0:
            dig = number % 10
            sum = sum + dig * (8 ** i)
            number = number // 10
            i = i + 1
        return sum

    def dec_bin(number):
        My_list = []
        while number != 0:
            Rem = number % 2
            number = number // 2
            My_list.append(Rem)
        New_list = My_list[::-1]
        for element in New_list:
            print(element, end='')

    num_dec = oct_dec(number)
    dec_bin(num_dec)


def oct_hex(number):
    def oct_dec(number):
        sum = 0
        i = 0
        while number != 0:
            dig = number % 10
            sum = sum + dig * (8 ** i)
            number = number // 10
            i = i + 1
        return sum

    def dec_hex(number):
        hex_digits = "0123456789ABCDEF"
        hexadecimal = ""
        while number > 0:
            remainder = number % 16
            if remainder < 10:
                hexadecimal = str(remainder) + hexadecimal
            else:
                hexadecimal = hex_digits[remainder] + hexadecimal
            number //= 16
        print("Hexadecimal NUMBER:", hexadecimal)

    num_dec = oct_dec(number)
    dec_hex(num_dec)


def hex_bin(number):
    def hex_dec(number):
        hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                    'C': 12, 'D': 13, 'E': 14, 'F': 15}
        total_sum = 0
        power = 0
        for digit in reversed(number):
            total_sum += hex_dict[digit.upper()] * (16 ** power)
            power += 1
        return total_sum

    def dec_bin(number):
        My_list = []
        while number != 0:
            Rem = number % 2
            number = number // 2
            My_list.append(Rem)
        New_list = My_list[::-1]
        for element in New_list:
            print(element, end='')

    num = hex_dec(number)
    dec_bin(num)


def hex_oct(number):
    def dec_oct(number):
        My_list = []
        while number != 0:
            Rem = number % 8
            number = number // 8
            My_list.append(Rem)
        New_list = My_list[::-1]
        for element in New_list:
            print(element, end='')

    def hex_dec(number):
        hex_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
                    'D': 13, 'E': 14, 'F': 15}
        total_sum = 0
        power = 0
        for digit in reversed(number):
            total_sum += hex_dict[digit] * (16 ** power)
            power += 1
        return total_sum

    num = hex_dec(number)
    dec_oct(num)


def bin_dec(number):
    sum = 0
    i = 0
    while number != 0 and flag == 'True':
        dig = number % 10
        sum = sum + dig * (2 ** i)
        number = number // 10
        i = i + 1
    print('Binary number: ', sum)


def hex_dec(number):
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                'C': 12, 'D': 13, 'E': 14, 'F': 15}
    sum = 0
    power = 0
    for digit in reversed(number):
        sum += hex_dict[digit] * (16 ** power)
        power += 1
    print(sum)


def dec_bin(number):
    My_list = []
    while number != 0:
        Rem = number % 2
        number = number // 2
        My_list.append(Rem)
    New_list = My_list[::-1]
    for element in New_list:
        print(element, end='')


def dec_hex(number):
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while number > 0:
        remainder = number
        remainder = number % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = hex_digits[remainder] + hexadecimal
        number //= 16
    print("Hexadecimal NUMBER:", hexadecimal)


def oct_dec(number):
    sum = 0
    i = 0
    while number != 0:
        dig = number % 10
        sum = sum + dig * (8 ** i)
        number = number // 10
        i = i + 1
    print('Decimal number:', sum)


def bin_dec(number):
    sum = 0
    i = 0
    while number != 0:
        dig = number % 10
        sum = sum + dig * (2 ** i)
        number = number // 10
        i = i + 1
    print('Binary number: ', sum)


valid = '0123456789ABCDEF'
while True:
    print('\n** numbering system converter **\n')
    print('A) insert a new number')
    print('B) Exit program\n')
    answer = str(input('Enter your choice: '))

    if answer == 'A':
        while True:
            number = input('Enter your number: ').upper()
            has_decimal = False
            for digit in number:
                if digit == '.':
                    has_decimal = True
                    break

            if has_decimal:
                print("Enter a valid number")
            else:
                break

        print('* Please select the base you want to convert a number from*')
        print('A) Decimal  ')
        print('B) Binary  ')
        print('C) Octal  ')
        print('D) Hexadecimal  ')
        answer1 = str(input('Enter your choice: '))
        print('* Please select the base you want to convert a number to *')
        print('A) Decimal  ')
        print('B) Binary  ')
        print('C) Octal  ')
        print('D) Hexadecimal  ')
        answer2 = str(input('Enter your choice: '))

        if answer1 == 'A' and answer2 == 'A':
            print('Your number = ', number)
        elif answer1 == 'A' and answer2 == 'B':
            dec_bin(int(number))
        elif answer1 == 'A' and answer2 == 'C':
            dec_oct(int(number))
        elif answer1 == 'A' and answer2 == 'D':
            dec_hex(int(number))
        if answer1 == 'B' and answer2 == 'B':
            print(number)
        elif answer1 == 'B' and answer2 == 'A':
            bin_dec(int(number))
        elif answer1 == 'B' and answer2 == 'C':
            bin_oct(int(number))
        elif answer1 == 'B' and answer2 == 'D':
            bin_hex(int(number))
        if answer1 == 'C' and answer2 == 'A':
            oct_dec(int(number))
        elif answer1 == 'C' and answer2 == 'D':
            oct_hex(int(number))
        elif answer1 == 'C' and answer2 == 'B':
            oct_bin(int(number))
        elif answer1 == 'C' and answer2 == 'C':
            print(number)
        if answer1 == 'D' and answer2 == 'D':
            print(number)
        elif answer1 == 'D' and answer2 == 'A':
            hex_dec(number)
        elif answer1 == 'D' and answer2 == 'B':
            hex_bin(number)
        elif answer1 == 'D' and answer2 == 'C':
            hex_oct(number)
    elif answer == 'B':
        break
    else:
        print('Please select a valid choice')