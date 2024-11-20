def min_leg_movements(instructions):
    n = len(instructions)
    if n <= 1:
        return 0

    positions = ["up", "down", "left", "right"]
    dp = {}

    # Initialize for first instruction
    for pos1 in positions:
        for pos2 in positions:
            if pos1 != pos2:
                dp[(0, pos1, pos2)] = 0

    # Process each instruction
    for i in range(n):
        target = instructions[i]
        new_dp = {}

        for pos1 in positions:
            for pos2 in positions:
                if pos1 != pos2 and (i, pos1, pos2) in dp:
                    curr_moves = dp[(i, pos1, pos2)]

                    if pos1 == target or pos2 == target:
                        key = (i + 1, pos1, pos2)
                        new_dp[key] = min(new_dp.get(key, float("inf")), curr_moves)
                    else:
                        key = (i + 1, target, pos2)
                        new_dp[key] = min(new_dp.get(key, float("inf")), curr_moves + 1)

                        key = (i + 1, pos1, target)
                        new_dp[key] = min(new_dp.get(key, float("inf")), curr_moves + 1)

        dp = new_dp

    min_moves = float("inf")
    for pos1 in positions:
        for pos2 in positions:
            if pos1 != pos2 and (n, pos1, pos2) in dp:
                min_moves = min(min_moves, dp[(n, pos1, pos2)])

    return min_moves


# Read input
N = int(input())
instructions = []
for _ in range(N):
    instructions.append(input().strip())

# Print output without any extra spaces or newlines
print(min_leg_movements(instructions), end="")
