# Explaining the math:
# Let B = blue discs and Let A = all discs
# We need to find (B/A) * (B-1/A*B-1) = 1/2 so transforming, and we get 2*B*(B-1) = A*(A-1) opening, and we get 2*B^2 - 2*B = A^2 - A
# Transforming it into Pell's standard equation we get: (4*B-2)^2 - 2*(2*A-1)^2 = 2   meaning: X = 4*B-2, Y = 2*A-1, D = 2, c = 2
# Finally from that we get: next_B = 3 * B + 2 * A - 2, next_A = 4 * B + 3 * A - 3    and looping through them until A is bigger then the requested we will get what we are looking for
def find_first_over(limit):
    blue, all_discs = 1, 1
    while all_discs <= limit:
        next_blue, next_all_discs = 3 * blue + 2 * all_discs - 2, 4 * blue + 3 * all_discs - 3
        blue, all_discs = next_blue, next_all_discs
    return {'all' :all_discs, 'blue' :blue, 'red' :all_discs - blue}

if __name__ == '__main__':
    n = int(input("Enter the limit: ")) # Inputs the minimal number we will start to check for the minimal number higher than it
    print(find_first_over(n)) # Prints how many discs all together and how many blue and how many red for the minimal amount higher than limit