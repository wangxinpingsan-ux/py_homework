bonus = ["1000", "2500", "3000"]

change=lambda x:x+"元"

bonus_change=list(map(change,bonus))
print(bonus_change)