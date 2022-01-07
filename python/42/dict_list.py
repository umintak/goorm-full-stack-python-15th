S1 = {1, 3}
S2 = {2, 3}

print(S1 & S2)
print(S1 | S2)
print(S1 - S2)

S1.add('goorm')
print(S1)

odd_list = set([5,'odd'])
S2.update(odd_list)
print(S2)

S2.remove(5)
print(S2)