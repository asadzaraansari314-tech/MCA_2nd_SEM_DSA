# Activity Selection using Greedy Algorithm

def activity_selection(start, finish):
    n = len(start)

    print("Selected Activities:")

    # Select first activity
    i = 0
    print(i, end=" ")

    # Select remaining activities
    for j in range(1, n):
        if start[j] >= finish[i]:
            print(j, end=" ")
            i = j

# Start and Finish times (sorted by finish time)
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

activity_selection(start, finish)
