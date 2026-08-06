candidates = [
    {"hours": 5,
     "score": 80},
    {"hours": 8,
     "score": 90},
    {"hours": 3,
     "score": 60},
    {"hours": 6,
     "score": 75},
    {"hours": 9,
     "score": 95}
]
closest_candidate = 0
similarity = 10000000
candidate_names = ["Amalya", "Vedant", "Haricharan", "Maya", "Leo"]
target = {"hours": int(input("hours: ")), "score": int(input("score: "))}
for candidate in candidates:
    if abs((target["hours"] + target["score"]) - (candidate["hours"] + candidate["score"])) < similarity:
        similarity = abs((target["hours"] + target["score"]) - (candidate["hours"] + candidate["score"]))
        closest_candidate = candidates.index(candidate)

print(candidate_names[closest_candidate])