# Gives every letter a value directly from Problem22.py
def letter_value(char):
    return ord(char.upper()) - ord('A') + 1 #ord() gives the Unicode (ASCII) number of the character , upper makes it uppercase

# Gives every word a value by giving every letter a value and summing them directly from Problem22.py
def give_value_to_words(all_the_words):
    word_values = {}
    for word in all_the_words:
        total = sum(letter_value(char) for char in word if char.isalpha())
        word_values[word] = total
    return word_values

# Finds all triangle numbers until n using the equation: T(n) = n(n+1)/2
def triangle_numbers(n):
    all_triangle_numbers = set()
    for i in range(n):
        all_triangle_numbers.add((i**2+i)//2)
    return all_triangle_numbers

# Finds all words whose letter-sum values are triangle numbers
def find_triangle_words(all_words):
    all_triangle_nums = triangle_numbers(100)
    word_values = give_value_to_words(all_words)
    triangle_words = []

    for word, value in word_values.items():
        if value in all_triangle_nums:
            triangle_words.append(word)

    return triangle_words


if __name__ == "__main__":
    user_input = input("Enter words separated by commas: ") # All the words you want to evaluate directly from Problem22.py
    words = [word.strip() for word in user_input.split(",") if word.strip()] # Inputs all the words directly from Problem22.py  
    print(len(find_triangle_words(words)), find_triangle_words(words))