scores = [78, 93, 62, 88]
print("Count:", len(scores))
print("Average:", round(sum(scores) / len(scores), 2))
for score in scores:
 label = "Pass" if score >= 50 else "Review"
print(score, label)

