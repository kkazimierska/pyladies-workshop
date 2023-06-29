# # define Python user-defined exceptions
# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass

# # you need to guess this number
# number = 18

# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")

# except InvalidAgeException:
#     print("Exception occurred: Invalid Age")

# Zadanie: Dodaj obsługę wieku +90.


# plik = open('some.txt')

try:
    plik = open('some.txt')
except FileNotFoundError:
    print("Proszę zdefiniować plik lub podać właściwą ścieżkę :)")