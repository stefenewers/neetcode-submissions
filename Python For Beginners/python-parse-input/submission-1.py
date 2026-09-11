from typing import List

def read_integers() -> List[int]:
    string = input()
    list_numbers = [int(x) for x in string.split(",")]
    return list_numbers

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
