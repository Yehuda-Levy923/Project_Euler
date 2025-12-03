# Returns list s where s[n] is the sum of proper divisors of n for n < limit
def sum_divisors(limit):
    s = [0] * limit
    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit, i):
            s[j] += i
    return s

# Finds the longest amicable chain with all members under limit
def longest_amicable_chain(limit):
    s = sum_divisors(limit)
    best, tid, visited = [], 1, [0] * limit

    for i in range(2, limit):
        if visited[i]:
            continue
        chain, pos = [], {}
        cur = i

        while True:
            if cur >= limit or cur == 0:
                break
            if not visited[cur]:
                visited[cur], pos[cur] = tid, len(chain)
                chain.append(cur)
                cur = s[cur]
                continue
            if visited[cur] == tid:
                cycle = chain[pos[cur]:]
                if len(cycle) > len(best): best = cycle
            break

        for n in chain: visited[n] = -1
        tid += 1

    return best


if __name__ == "__main__":
    num = int(input("Enter the highest number of chain you want: ")) # Inputs the highest number of the chain that you want to check
    longest_chain = longest_amicable_chain(num) # Finds the longest amicable chain with numbers under n to halve computing time
    print(longest_chain, "\n", min(longest_chain)) # Prints the longest amicable chain with numbers under n and its smallest member