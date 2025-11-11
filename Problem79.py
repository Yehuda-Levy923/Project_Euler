# Answered with pen & paper in under 30 secs: 73162890
# Reconstruct the shortest possible passcode from a bunch of subsequences. Each subsequence tells us "this digit comes before that digit".
def reconstruct_passcode(sequences):
    graph = {}
    indegree = {}

    for seq in sequences:
        for ch in seq:
            if ch not in graph:
                graph[ch] = []
            if ch not in indegree:
                indegree[ch] = 0

        for i in range(len(seq) - 1):
            a, b = seq[i], seq[i + 1]
            if b not in graph[a]:
                graph[a].append(b)
                indegree[b] += 1

    queue = [ch for ch in indegree if indegree[ch] == 0]
    passcode = ""

    while queue:
        current = queue.pop(0)
        passcode += current
        for nxt in graph[current]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return passcode


if __name__ == "__main__":
    print("Enter subsequences (one per line). Empty line to finish:")
    subsequences = []
    while True:
        line = input().strip()
        if not line:
            break
        subsequences.append(line)

    print(reconstruct_passcode(subsequences))