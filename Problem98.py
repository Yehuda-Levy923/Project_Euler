# Read words
def input_all_words_separated_by_commas():
    words = input("Enter words: ")
    return [word.strip().strip('"') for word in words.split(',')]

# Sort words by length (descending)
def sort_words_by_length(words):
    return sorted(words, key=len, reverse=True)

# Precompute squares up to limit (=10^7)
def precalc_squares(limit=10**7):
    squares = {}
    for i in range(1, limit+1):
        sq = str(i*i)
        squares.setdefault(len(sq), []).append(sq)
    return squares

# Check if two words are anagrams
def is_anagram(w1, w2):
    return sorted(w1) == sorted(w2)

# Check if mapping word → square is valid
def is_valid_mapping(word, square):
    mapping, reverse = {}, {}
    for w, s in zip(word, square):
        if w in mapping and mapping[w] != s:
            return None
        if s in reverse and reverse[s] != w:
            return None
        mapping[w] = s
        reverse[s] = w
    return mapping

# Apply mapping to another word
def apply_mapping(word, mapping):
    return ''.join(mapping[c] for c in word)

# Function to find the largest square number formed by anagramic words from the list
def find_largest_square():
    words = sort_words_by_length(input_all_words_separated_by_commas())
    squares_by_length = precalc_squares()

    max_square = 0
    for i, word1 in enumerate(words):
        for word2 in words[i+1:]:
            if len(word1) != len(word2):
                break
            if not is_anagram(word1, word2):
                continue

            n = len(word1)
            if n not in squares_by_length:
                continue

            for square in squares_by_length[n]:
                mapping = is_valid_mapping(word1, square)
                if mapping:
                    candidate = apply_mapping(word2, mapping)
                    if candidate in squares_by_length[n] and candidate[0] != '0':
                        max_square = max(max_square, int(square), int(candidate))
                        return max_square  # return immediately if found
    return max_square


if __name__ == "__main__":
    print("Maximum square number found:", find_largest_square()) # Output the maximum square number found