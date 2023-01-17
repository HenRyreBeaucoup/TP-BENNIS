from collections import Counter

L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
count = Counter(L1)
most_common_element, frequency = count.most_common(1)[0]
print("Le nombre le plus fréquent dans la liste est le : {} ({} x)".format(most_common_element, frequency))