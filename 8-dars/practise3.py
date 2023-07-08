taomlar = ['pitsa', 'osh', 'shashlik', 'mastava', 'somsa']

nonushta = taomlar[:]
nonushta.remove('osh')
nonushta.remove('pitsa')
nonushta.remove('somsa')
nonushta.append('shirin guruch')
nonushta.append('pirog')

print("Taomlar: ", taomlar, "\n" "Nonushta: ",nonushta)

nonushta = tuple(nonushta)
nonushta.append("qaymoq va non")

# done