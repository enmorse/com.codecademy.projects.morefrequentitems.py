# Write your function here
def more_frequent_item(lst, item1, item2):
    return [item1 if lst.count(item1) >= lst.count(item2) else item2]


print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
