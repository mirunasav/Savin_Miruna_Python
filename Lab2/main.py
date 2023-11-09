# 1.  Write a function to return a list of the first n numbers in the Fibonacci string.


def fibonacci():
    n = int(input("Write a number : "))
    fibonacci_list = []
    first, second = 0, 1
    for i in range(n):
        fibonacci_list.append(first)
        first, second = second, first + second
    for i in fibonacci_list:
        print(i)
    return fibonacci_list


# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def prime_numbers(numbers):
    prime_numbers_list = [number for number in numbers if
                          len([y for y in range(2, number // 2 + 1) if number % y == 0]) == 0]
    return prime_numbers_list


# 3. Write a function that receives as parameters two lists a and b and returns:
# (a intersected with b, a reunited with b, a - b, b - a)

def operations(a, b):
    intersection = list(set(a).intersection(set(b)))
    union = list(set(a).union(set(b)))
    a_minus_b = list(set(a).difference(set(b)))
    b_minus_a = list(set(b).difference(set(a)))

    return intersection, union, a_minus_b, b_minus_a


# 4.
def composition(notes, moves, start_position):
    song = [notes[start_position]]
    current_position = start_position

    for move in moves:
        current_position = (current_position + move) % len(notes)
        song.append(notes[current_position])

    print(song)

composition(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
# 5. replace matrix elements under the main diagonal with 0

def replace_matrix_elements(matrix):
    num_rows = len(matrix)

    for i in range(num_rows):
        for j in range(0, i):
            matrix[i][j] = 0

    return matrix


# 6.
def items_appearing_x_times(x, *lists):
    concatenated_list = [item for sublist in lists for item in sublist]
    counter = {}
    list_of_items_appearing_x_times = []

    for item in concatenated_list:
        if item not in counter:
            counter[item] = 0
        counter[item] += 1

    for item in counter.keys():
        if counter.get(item) == x:
            list_of_items_appearing_x_times.append(item)
    return list_of_items_appearing_x_times


# 7.
def number_of_palindromes(list_of_numbers):
    palindromes = [number for number in list_of_numbers if str(number) == str(number)[::-1]]
    max_palindrome = max(palindromes)
    return len(palindromes), max_palindrome


# 8.
def ascii_codes_divisible_by_x(x=1, strings=[], flag=True):
    list_of_character_lists = []
    for string in strings:
        characters_divisible_with_x = []
        for character in string:
            if (ord(character) % x == 0) == flag:
                characters_divisible_with_x.append(character)
        list_of_character_lists.append(characters_divisible_with_x)

    return list_of_character_lists


print(ascii_codes_divisible_by_x(2, ["test", "hello", "lab002"], False))


# 9. Spectators who cannot see

def spectators_who_cannot_see(matrix):
    num_rows = len(matrix)

    if num_rows <= 1:
        return []

    num_columns = len(matrix[0])

    sad_spectators = []

    for row_of_spectator in range(1, num_rows):
        for j in range(num_columns):
            for row_in_front_of_spectator in range(row_of_spectator):
                if matrix[row_in_front_of_spectator][j] > matrix[row_of_spectator][j]:
                    sad_spectators.append((row_of_spectator, j))
                    break

    return sad_spectators

print(spectators_who_cannot_see([[1, 2, 3, 2, 1, 1],

[2, 4, 4, 3, 7, 2],

[5, 5, 2, 5, 6, 4],

[6, 6, 7, 6, 7, 5]] ))

# 10.
def tuples_with_numbers_from_same_position(*lists):
    numbers_from_the_same_position = []

    max_length = max([len(x) for x in lists])

    for position in range(max_length):
        tuple_of_numbers = tuple(list_of_numbers[position]
                                 if len(list_of_numbers) >= position + 1 else None
                                 for list_of_numbers in lists)
        numbers_from_the_same_position.append(tuple_of_numbers)

    for tuple_of_numbers in numbers_from_the_same_position:
        print(tuple_of_numbers)
    return numbers_from_the_same_position


# 11.
def sort_tuples_by_second_element_character(tuples_list):
    sorting_key = lambda x: x[1][2] if len(x[1]) >= 3 else ''

    sorted_tuples = sorted(tuples_list, key=sorting_key)
    return sorted_tuples


# 12.
# intrebare dc nu merge cu  dictionary_of_rhymes.get(word[-2:], []) dar merge cu setdefault? si asta dinainte merge cu 0
def group_words_by_rhyme(list_of_words):
    dictionary_of_rhymes = {}

    for word in list_of_words:
        dictionary_of_rhymes.setdefault(word[-2:], []).append(word)

    for rhyme_groups in dictionary_of_rhymes.keys():
        print(dictionary_of_rhymes[rhyme_groups])


group_words_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte'])
