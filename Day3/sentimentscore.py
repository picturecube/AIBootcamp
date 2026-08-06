positive_words = {"love": 2, "great": 2, "good": 1, "amazing": 3}
negative_words = {"hate": -2, "bad": -1, "bugs": -1, "boring": -2}
sentence = input("Enter a sentence: ").lower().split()
score = 0
for word in sentence:
    if word in positive_words:
        score += positive_words[word]
    elif word in negative_words:
        score += negative_words[word]
print(score)
print("Positive" if score > 0 else "Negative" if score < 0 else "Neutral")