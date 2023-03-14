# Algorithimc-Thinking-Python-Solutions
This repository contains solutions to all the tasks presented in the book "Algorithmic Thinking" by Daniel Zingaro in Python

## Snowflakes Code description 

This code defines a class named SnowflakesCounter which takes a list of snowflakes as input. It then defines three methods:

**__init__**: initializes three instance variables of the class: snowflakes, count_snowflakes, and same_list.

**sorted_snowflakes**: sorts each snowflake in the input list in ascending order and returns the sorted list of snowflakes.

**count_equal_lists**: calls the sorted_snowflakes method to obtain the sorted list of snowflakes, then compares each pair of snowflakes in the list to check for equality. If two snowflakes are equal, it adds them to the same_list and increments their count in the count_snowflakes dictionary.

**print_results**: calls the count_equal_lists method, then prints the total number of equal lists and the lists that have a pair in the same_list.

The main function creates an instance of the SnowflakesCounter class with a list of snowflakes as input, and calls the print_results method to display the results.

In summary, this code takes a list of snowflakes as input, and checks if there are any duplicate snowflakes. If duplicates are found, it returns the total number of equal lists and the lists that have a pair.
