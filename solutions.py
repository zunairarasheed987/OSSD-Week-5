times = [120, 45, 32, 28, 41, 39, 35, 210]
result1 = times[2:-2][::-1]
print("Task 1:", result1)

tasks = ["done", "pending", "done", "pending", "done", "pending"]
tasks[1::2] = ["completed"] * len(tasks[1::2])
tasks[3:3] = ["audit"]
print("Task 2:", tasks)

points = [(2, 5), (8, 3), (4, 4), (9, 1)]
result3 = [(y, x) if x > y else (x, y) for x, y in points]
print("Task 3:", result3)

raw_temps = [22.5, "ERR", 18.0, None, 30.2, "ERR", 0.0]
result4 = [round(c * 1.8 + 32, 1) for c in raw_temps if isinstance(c, (int, float))]
print("Task 4:", result4)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal = [matrix[i][i] for i in range(len(matrix))]
evens = [num for row in matrix for num in row if num % 2 == 0]
print("Task 5: Diagonal:", diagonal)
print("Task 5: Evens:", evens)

prices = [100, 102, 104, 103, 105, 110]
k = 3
result6 = [(i, round(sum(prices[i:i + k]) / k, 2)) for i in range(len(prices) - k + 1)]
print("Task 6:", result6)

players = [("Aria", 88, True), ("Kael", 95, False), ("Zane", 91, True),
           ("Mira", 76, True), ("Lyra", 99, True), ("Dax", 84, True)]
active = [p for p in players if p[2]]
top3 = sorted(active, key=lambda p: p[1], reverse=True)[:3]
result7 = [f"Rank {n}: {name} ({score})" for n, (name, score, _) in enumerate(top3, 1)]
print("Task 7:", result7)

odometer = (1050, 1085, 1120, 1200, 1215)
result8 = [(s, e, e - s) for s, e in zip(odometer[:-1], odometer[1:])]
print("Task 8:", result8)
