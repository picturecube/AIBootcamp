low = 0
high = 7
target = float(input("Enter a target score (0-1): "))
scores = [0.12, 0.35, 0.41, 0.58, 0.63, 0.77, 0.89, 0.95]
def search(high, low, scores):
    mid = (high + low) // 2
    if scores[mid] >= target:
        return mid
    else:
        return search(high, mid + 1, scores)
print(search(high, low, scores))