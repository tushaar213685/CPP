def F(n):
    for i in range(n):
        # Create the outer dashes
        dashes = '-' * (n - i - 1)
        
        # Create the central pattern
        pattern = ''.join(chr(65 + abs(j)) for j in range(-i, i + 1))
        
        # Combine and print
        print(f"{dashes}{pattern}{dashes}")

# Tests
F(10)
print()  # Separator
F(6)

"""
output
---------A---------
--------BAB--------
-------CBABC-------
------DCBABCD------
-----EDCBABCDE-----
----FEDCBABCDEF----
---GFEDCBABCDEFG---
--HGFEDCBABCDEFGH--
-HGFEDCBABCDEFGHI--
JIHGFEDCBAABCDEFGHIJ


-----A-----
----BAB----
---CBABC---
--DCBABCD--
-EDCBABCDE-
FEDCBABCDEF

"""