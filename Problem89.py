# Function that converts a Roman numeral string to its integer value
def roman_to_integer(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    total = prev = 0
    for ch in reversed(s):
        val = roman_map[ch]
        total += val if val >= prev else -val
        prev = val
    return total

# Function that converts an integer to its minimal Roman numeral representation
def integer_to_minimal_roman(n):
    value_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                 (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                 (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ''
    for val, sym in value_map:
        while n >= val:
            result += sym
            n -= val
    return result

# Function that calculates total characters saved by converting to minimal Roman form
def total_characters_saved(roman_list):
    saved = 0
    for roman in roman_list:
        original_length = len(roman)
        minimal_length = len(integer_to_minimal_roman(roman_to_integer(roman)))
        saved += original_length - minimal_length
    return saved


# Function that reads Roman numerals from user input
def read_roman_input():
    print("Enter Roman numerals (one per line). Press Enter twice to finish:\n")
    return [line.strip() for line in iter(input, '') if line.strip()]


if __name__ == '__main__':
    roman_list = read_roman_input()  # Inputs a list of Roman numerals from the user
    print(total_characters_saved(roman_list))  # Outputs the total number of characters saved by minimizing them