def convert_nums_to_words(num):
    words = ""

    # lists for converting single digits, teens and tens to words
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    # converts thousands place to words
    thousands = num // 1000
    if thousands > 0:
        words += ones[thousands] + "thousand"
        num %= 1000  # remove thousands part from word

    # converts hundreds place to words and adds 'and' if num%100 != 0
    hundreds = num // 100
    remainder = num % 100
    if hundreds > 0:
        words += ones[hundreds] + "hundred"
        if remainder != 0:
            words += "and"

    # converts tens+ones place to words does teens if needed
    if 10 <= remainder <= 19:
        words += teens[remainder - 10]
    else:
        t = remainder // 10
        u = remainder % 10
        if t > 0:
            words += tens[t]
        if u > 0:
            words += ones[u]

    return words

# converts every number from 1 up to num into words and sums their character lengths
def add_all_length_until(num1, num2):
    length_of_all = 0
    for i in range(num1,num2+1):
        print(convert_nums_to_words(i), " length:" ,len(convert_nums_to_words(i)))
        length_of_all = len(convert_nums_to_words(i)) + length_of_all
    return length_of_all

if __name__ == '__main__':
    n = int(input("Enter a number to start (between 1 - 9999): ")) # inputs value of n that we will add the lengths of the words from
    m = int(input("Enter a number to finish (between 1 - 9999): ")) # inputs value of m that we will add the lengths of the words until
    print(add_all_length_until(n,m)) #prints the sum of all the lengths of n until m