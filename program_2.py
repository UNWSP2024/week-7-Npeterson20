# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all of the numbers in the list that are greater than then number n.

def larger_than_n(numbers, n):
    print("Numbers greater than", n, ":")
    for number in numbers:
        if number > n:
            print(number)

# Example usage
numbers_list = [10, 25, 30, 15, 50, 5]
n_value = 20
larger_than_n(numbers_list, n_value)
