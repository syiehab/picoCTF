import string

flag = []

with open('basic mod\message.txt') as file:
    content = file.read()
    numbers = [int(val) for val in content.split()]
    print(numbers)

    
    for num in numbers:
        modular = pow(num, -1, 41)
        
        if modular in range(1, 27):
            flag.append(string.ascii_uppercase[modular-1])
        elif modular in range(27, 36):
            flag.append(string.digits[modular-27])
        elif modular == 37:
            flag.append('_')

    print(flag)


print('picoCTF{%s}' % ''.join(flag))

