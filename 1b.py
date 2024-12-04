def F(d: dict):
    # Sorting by key (ascending)
    print("Sorted by key (ascending):")
    for key in sorted(d.keys()):
        print(f"-{key}-, -{d[key][0]}-, -{d[key][1]}-")
    
    # Sorting by x (descending)
    print("\nSorted by x (descending):")
    for key in sorted(d.keys(), key=lambda k: d[k][0], reverse=True):
        print(f"-{key}-, -{d[key][0]}-, -{d[key][1]}-")
    
    # Sorting by y (ascending)
    print("\nSorted by y (ascending):")
    for key in sorted(d.keys(), key=lambda k: d[k][1]):
        print(f"-{key}-, -{d[key][0]}-, -{d[key][1]}-")

# Tests
F({1: (1, 2), 2: (-1, 4), 5: (-4, 3), 4: (2, 3)})
print()  # Separator
F({-8: (4, 2), 6: (-3, 4), 7: (2, 1), 5: (9, -10)})

"""
output
Sorted by key (ascending):
-1-, -1-, -2-
-2-, --1-, -4-
-4-, -2-, -3-
-5-, --4-, -3-

Sorted by x (descending):
# By '3' output next.




Sorted by key (ascending):
-1-, -1-, -2-
-2-, --1-, -4-
-4-, -2-, -3-
-5-, --4-, -3-

Sorted by x (descending):
2-4-, --3-, -sorted output By 'X' with descending Order from the given tuple
"""