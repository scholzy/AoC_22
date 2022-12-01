#!/usr/bin/env python3

from _api import get_input

def main():
    data = get_input(1).splitlines()

    calorie_counts = []

    current_calories = 0
    for item in data:
        if item == '':
            calorie_counts.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(item)

    # In-place to avoid repeating sorting it for parts 1 and 2
    calorie_counts.sort(reverse=True)

    # Part 1 answer
    print(f"The maximum calorie count is {calorie_counts[0]}")

    # Part 2 answer
    top_three_counts = sum(calorie_counts[:3])
    print(f"The sum of the top three counts is {top_three_counts}")

if __name__ == '__main__':
    main()