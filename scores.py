scores = [81, 67, 93, 58, 76, 88]
passed = [score for score in scores if score >= 60]
average = sum(scores) / len(scores)
print('Average:', round(average, 1))
print('Passed:', len(passed))
print('Highest:', max(scores))

