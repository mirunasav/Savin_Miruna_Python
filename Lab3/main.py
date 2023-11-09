# 1. Write a function that receives as parameters two lists a and b and returns \
# a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
def lists_to_sets(a, b):
    list_of_sets = []
    set_a = set(a)
    set_b = set(b)
    list_of_sets.append(set_a.intersection(set_b))
    list_of_sets.append(set_a.union(set_b))
    list_of_sets.append(set_a.difference(set_b))
    list_of_sets.append(set_b.difference(set_a))
    return list_of_sets


# 2. character appearances in string
def character_appearances_in_string(a):
    character_appearances = {}
    for char in a:
        character_appearances[char] = character_appearances.get(char, 0) + 1
    for key in character_appearances.keys():
        print(key, character_appearances[key])
    return character_appearances

# 3. compare two dictionaries
def compare_dictionaries(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        if set(dict1.keys()) != set(dict2.keys()):
            return False
        for key in dict1.keys():
            # recursively compare components
            if not compare_dictionaries(dict1[key], dict2[key]):
                return False
        return True
    else:
        return dict1 == dict2


# 4. build xml tags
# * -> arguments : any non-keyword arguments => passed as tuple
# ** -> key word arguments (kwargs) ex banana = 1, etc => passed as dictionary
def build_xml_element(tag, content, **key_value_elements):
    opening_tag = f"<{tag}"
    for key, value in key_value_elements.items():
        opening_tag += f' {key}="{value}"'
    opening_tag += f">"

    closing_tag = f"</{tag}>"
    xml_element = f"{opening_tag}{content}{closing_tag}"

    return xml_element


# 5. validate dictionary: all values start with prefix, have a middle and end with suffix
def validate_dict(rules, dictionary):
    for key, preffix, middle, suffix in rules:
        if key not in dictionary:
            return False

        value = dictionary[key]
        value_length = len(value)

        if not value.startswith(preffix) or not value.endswith(suffix):
            return False

        middle_start_index = value.find(middle)
        middle_end_index = middle_start_index + len(middle)

        if middle_start_index < len(preffix) or middle_end_index >= value_length - len(suffix):
            return False

    return True

print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")} , {"key1": "come inside, it's too cold out", "key3": "this is not valid"} ))
# 6. return number of unique and duplicate elements
def unique_and_duplicate_number(a):
    set_a = set(a)

    duplicates = len(a) - len(set(a))
    unique = len(a) - duplicates * 2

    return unique, duplicates


# 7. sets and operations dictionary
def sets_operations_dictionary(*sets):
    number_of_sets = len(sets)
    if number_of_sets < 2:
        return

    operation_dictionary = {}

    for i in range(number_of_sets):
        for j in range(i + 1, number_of_sets):
            set_1 = set(sets[i])  # or just sets[i]
            set_2 = set(sets[j])
            operation_dictionary[f"{set_1} | {set_2}"] = set_1.union(set_2)  # or set_1 | set_2
            operation_dictionary[f"{set_1} & {set_2}"] = set_1.intersection(set_2)  # or set_1 & set_2
            operation_dictionary[f"{set_1} - {set_2}"] = set_1.difference(set_2)  # or set_1 - set_2
            operation_dictionary[f"{set_2} - {set_1}"] = set_2.difference(set_1)

    return operation_dictionary


# 8. dictionary mapping / travel
def dictionary_traversal(mapping):
    list_of_traversed_objects = []

    next_value = mapping['start']
    while True:
        list_of_traversed_objects.append(next_value)
        # next_value = mapping[next_value] : what if the dictionary does not have this value?
        next_value = mapping.get(next_value, None)
        if next_value in list_of_traversed_objects or next_value is None:
            break

    return list_of_traversed_objects

print(dictionary_traversal({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
# 9. variable number of arguments found in kwargs
def number_of_pos_arguments_in_kwargs(*args, **kwargs):
    number = 0
    for value in kwargs.values():
        if value in args:
            number += 1

    return number


def number_of_pos_arguments_in_kwargs_2(*args, **kwargs):
    number = 0

    kw_values = set(kwargs.values())
    for arg in args:
        if arg in kw_values:
            number += 1

    return number

