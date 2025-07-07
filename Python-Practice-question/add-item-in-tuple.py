def add(tup,item):
    return tup + (item,)

# Example usage:
tup = (1, 2, 3)
item = 4
new_tup = add(tup, item)
print(new_tup)  # Output: (1, 2, 3, 4)