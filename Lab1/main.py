import math


# 1.Find The greatest common divisor of multiple numbers read from the console.

def find_gcd():
    numbers = list(map(int, input("write some numbers ").split(" ")))
    gcd = numbers[0]

    for number in numbers[1:]:
        gcd = math.gcd(gcd, number)

    output = "gcd is : " + str(gcd)
    print(output)
    return gcd


# 2.Write a script that calculates how many vowels are in a string.
def number_of_vowels():
    string = input("write a word: ")
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for character in string:
        if character in vowels:
            vowel_count += 1

    print(f"the number of vowels is :{vowel_count}")
    return vowel_count


# 3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def number_of_string_appearance():
    str1 = input("first string: ")
    str2 = input("second string: ")

    count = 0
    start = 0
    while start < len(str2):
        index = str2.find(str1, start)
        if index != -1:
            count += 1
            start = index + 1
        else:
            break
    print(f"number of occurences: {count}")
    return count


# 4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
def convert_upper_camel_case_to_underscore_to_snake_case():
    camel_case_string = input("write a camel case string: ")
    snake_case_string = ""
    for char in camel_case_string:
        if char.isupper() and snake_case_string:
            snake_case_string += '_'
        snake_case_string += char.lower()

    print(f"snake case string: {snake_case_string}")
    return snake_case_string


# 5. Read the word in the matrix in spiral order
def spiral_order_reading(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append((row.pop()))
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    print(''.join(result))


# 6. Write a function that validates if a number is a palindrome.
def is_number_palindrome(number):
    number_as_string = str(number)

    return number_as_string == number_as_string[::-1]


# 7. extract first number from text
def extract_first_number_from_text():
    text = input("write some text with a number in it ")
    number = ""
    found_digit = False

    for char in text:
        if char.isdigit():
            number += char
            found_digit = True
        elif found_digit:
            break

    if number:
        print(f"the number is : {number}")
        return
    print("no number was found")


# 8. count number of bits of 1 in number
def number_of_1_bits(number):
    number_in_binary_as_string = str(bin(number))
    count = 0

    for bit in number_in_binary_as_string:
        if bit == '1':
            count += 1

    print(count)


# 9. most common letter:
def most_common_letter(string):
    lower_case_string = string.lower()
    letter_occurence = {}
    for char in lower_case_string:
        if char.isalpha():
            letter_occurence[char] = letter_occurence.get(char, 0) + 1
    most_common = max(letter_occurence, key=letter_occurence.get)

    print(f"{most_common}, {letter_occurence[most_common]}")
    return most_common, letter_occurence[most_common]


# 10. number of words in a text (separated by one space only)
def number_of_words(text):
    count = 0
    words = text.split()
    for word in words:
        if word != ' ':
            count += 1

    print(f"number of words : {count}")


'''
spiral_order_reading([
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
])
'''



