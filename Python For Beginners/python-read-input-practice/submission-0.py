import sys 
def add_two_numbers() -> int:
    numbers = [int(x) for x in sys.stdin.readline().split(',')]
    return sum(numbers)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
