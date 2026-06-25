scores = [45, 82, 59, 90, 74, 30]

passgrade = lambda x :x>=60

pass_score=list(filter(passgrade,scores))
print(pass_score)