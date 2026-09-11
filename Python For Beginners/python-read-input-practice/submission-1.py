def add_two_numbers() -> int:
    nums = input()
    list_of_nums = [int(x) for x in nums.split(",")]
    sum_of_nums = list_of_nums[0] + list_of_nums[1]
    return sum_of_nums



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
