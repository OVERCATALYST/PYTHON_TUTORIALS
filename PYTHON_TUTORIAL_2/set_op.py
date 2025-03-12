def set_operations(set1,set2):
    union=set1|set2
    intersection=set1&set2
    difference=set1-set2
    symmetric_difference=set1^set2
    return union,intersection,difference,symmetric_difference

s1=set(map(int,input("Enter elements of first set: ").split()))
s2=set(map(int,input("Enter elements of second set: ").split()))

union,intersection,difference,symmetric_difference=set_operations(s1,s2)

print("Union:",union)
print("Intersection:",intersection)
print("Difference (Set1 - Set2):",difference)
print("Symmetric Difference:",symmetric_difference)
