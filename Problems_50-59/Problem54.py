# Function that reads input lines and returns two lists of hands (player1 and player2)
def all_poker_hands():
    total_hands = int(input("How many poker hands? ").strip())
    p1_hands = []
    p2_hands = []
    for _ in range(total_hands):
        tokens = input().upper().split()
        if len(tokens) != 10:
            raise ValueError("Each line must contain 10 cards: 5 for player1 and 5 for player2")
        p1_hands.append(tokens[:5])
        p2_hands.append(tokens[5:])
    return p1_hands, p2_hands

# Function that assigns a numeric category strength to a 5-card hand (1..10)
def strength(hand):
    royal_flush, strait_flush, four, full_house, flush, strait, three, two_pairs, pair, high = 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    rank_map = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
    }
    ranks = [rank_map[card[0]] for card in hand]
    suits = [card[1] for card in hand]

    ranks.sort()

    counts = {}
    for r in ranks:
        counts[r] = counts.get(r, 0) + 1
    freq = sorted(counts.values(), reverse=True)

    is_flush = len(set(suits)) == 1

    is_straight = (ranks == [2, 3, 4, 5, 14]) or all(ranks[i] + 1 == ranks[i + 1] for i in range(4))


    if ranks == [10, 11, 12, 13, 14] and is_flush:
        return royal_flush
    elif is_flush and is_straight:
        return strait_flush
    elif freq == [4, 1]:
        return four
    elif freq == [3, 2]:
        return full_house
    elif is_flush:
        return flush
    elif is_straight:
        return strait
    elif freq == [3, 1, 1]:
        return three
    elif freq == [2, 2, 1]:
        return two_pairs
    elif freq == [2, 1, 1, 1]:
        return pair
    else:
        return high

# Function that returns a tie-breaker list for comparing two hands within the same category
def tiebreaker(hand):
    royal_flush, strait_flush, four, full_house, flush, strait, three, two_pairs, pair, high = 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    rank_map = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
    }
    ranks = [rank_map[card[0]] for card in hand]
    suits = [card[1] for card in hand]

    ranks.sort()

    counts = {}
    for r in ranks:
        counts[r] = counts.get(r, 0) + 1
    freq = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    is_flush = len(set(suits)) == 1

    is_straight = (ranks == [2, 3, 4, 5, 14]) or all(ranks[i] + 1 == ranks[i + 1] for i in range(4))


    if ranks == [10, 11, 12, 13, 14] and is_flush:
        return [14]
    elif is_straight:
        return [5] if ranks == [2, 3, 4, 5, 14] else [max(ranks)]
    elif freq[0][1] == 4:
        return [freq[0][0], freq[1][0]]
    elif freq[0][1] == 3 and freq[1][1] == 2:
        return [freq[0][0], freq[1][0]]
    elif is_flush or strength(hand) == 1:
        return sorted(ranks, reverse=True)
    elif freq[0][1] == 3:
        kickers = [r for r, c in freq if c == 1]
        return [freq[0][0]] + sorted(kickers, reverse=True)
    elif freq[0][1] == 2 and freq[1][1] == 2:
        return [freq[0][0], freq[1][0], freq[2][0]]
    elif freq[0][1] == 2:
        kickers = [r for r,c in freq if c == 1]
        return [freq[0][0]] + sorted(kickers, reverse=True)

    return sorted(ranks, reverse=True)

# Function that compares two hands and returns the better hand or None if tie
def better_hand_checker(player1, player2):
    if strength(player1) > strength(player2):
        return player1
    if strength(player1) < strength(player2):
        return player2
    else:
        tb1, tb2 = tiebreaker(player1), tiebreaker(player2)
        if tb1 > tb2:
            return player1
        elif tb2 > tb1:
            return player2
        else:
            return None

# Function that counts how many of the input hand pairs are won by player1
def how_many_wins_for_player1():
    p1, p2 = all_poker_hands()
    p1_wins = 0
    for i in range(len(p1)):
        if better_hand_checker(p1[i],p2[i]) == p1[i]:
            p1_wins += 1
    return p1_wins

if __name__ == "__main__":
    print(how_many_wins_for_player1()) # run the program and print how many hands player1 won