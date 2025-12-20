#sorts names using merge sort
def sort_names(all_the_names):
    if len(all_the_names) <= 1:
        return all_the_names
    # divide the list into two halves
    mid = len(all_the_names) // 2
    left_half = all_the_names[:mid]
    right_half = all_the_names[mid:]
    # recursively sort both halves
    left_half = sort_names(left_half)
    right_half = sort_names(right_half)
    # merge the sorted halves
    return merge(left_half, right_half)

#part of merge sort
def merge(left, right):
    merged_list = []
    i = 0  # pointer for the left list
    j = 0  # pointer for the right list

    # compare elements from both lists and add the smaller one to merged_list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # lexicographical comparison for strings
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    # add any remaining elements from the left list
    while i < len(left):
        merged_list.append(left[i])
        i += 1

    # add any remaining elements from the right list
    while j < len(right):
        merged_list.append(right[j])
        j += 1

    return merged_list

#gives every letter a value
def letter_value(char):
    return ord(char.upper()) - ord('A') + 1 #ord() gives the Unicode (ASCII) number of the character , upper makes it uppercase

#gives every name a value by giving every letter a value and summing them
def give_value_to_names(all_the_names):
    name_values = {}
    for name in all_the_names:
        total = sum(letter_value(char) for char in name if char.isalpha())
        name_values[name] = total
    return name_values

#multiplies all the names_values by their placement then sums it all up
def find_total_score(all_the_names):
    sorted_names = sort_names(all_the_names)
    name_values = give_value_to_names(sorted_names)

    total_score = 0
    for i, name in enumerate(sorted_names):
        position = i + 1
        value = name_values[name]
        total_score += position * value

    return total_score


if __name__ == "__main__":
    user_input = input("Enter names separated by commas: ") #all the names you want to evaluate
    names = [name.strip() for name in user_input.split(",") if name.strip()] #inputs all the names
    print(find_total_score(names)) #finds and prints the final score