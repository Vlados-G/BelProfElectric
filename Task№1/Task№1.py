# Task№1
# Меняем байты местами

def swap_bytes(number):
    return (number >> 8) | ((number & 0xff) << 8)


# Вводим число
input_number = int(input("Введите число: "))
swapped_number = swap_bytes(input_number)
print(hex(swapped_number))
