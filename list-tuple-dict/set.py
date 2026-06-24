s1 = set([1, 2, 3])
s2 = set((3, 4, 5))
print(type(s1))

set_union = s1.union(s2)
print(set_union)

intersection = s1.intersection(s2)
print(intersection)

difference = s1.difference(s2)
print(difference)

symmetric_difference = s1.symmetric_difference(s2)
print(symmetric_difference)