# Algorithimc-Thinking-Python-Solutions
This repository contains solutions to all the tasks presented in the book "Algorithmic Thinking" by Daniel Zingaro in Python

Link: https://www.amazon.com/Algorithmic-Thinking-Problem-Based-Daniel-Zingaro-ebook/dp/B085BVJ51Z?ref_=ast_author_dp

## Snowflakes Code description 

This code defines a class named SnowflakesCounter which takes a list of snowflakes as input. It then defines three methods:

**__init__**: initializes three instance variables of the class: snowflakes, count_snowflakes, and same_list.

**sorted_snowflakes**: sorts each snowflake in the input list in ascending order and returns the sorted list of snowflakes.

**count_equal_lists**: calls the sorted_snowflakes method to obtain the sorted list of snowflakes, then compares each pair of snowflakes in the list to check for equality. If two snowflakes are equal, it adds them to the same_list and increments their count in the count_snowflakes dictionary.

**print_results**: calls the count_equal_lists method, then prints the total number of equal lists and the lists that have a pair in the same_list.

The main function creates an instance of the SnowflakesCounter class with a list of snowflakes as input, and calls the print_results method to display the results.

In summary, this code takes a list of snowflakes as input, and checks if there are any duplicate snowflakes. If duplicates are found, it returns the total number of equal lists and the lists that have a pair.

## CompoundWords Code description 

This code defines a function called find_compound_words() which takes in a list of words as an argument, and returns a list of all the compound words in the input list. A compound word is a word that can be formed by concatenating two or more smaller words that are also present in the input list.

The function loops through each word in the input list, and then loops through all the possible prefixes and suffixes of that word. It checks whether both the prefix and suffix are present in the input list, and if so, adds the current word to a list of compound words.

The function then returns the list of compound words.

###Steps:

* Define a list of words.
* Define a function called find_compound_words() that takes a list of words as an argument.
* Create an empty list called compound_words.
* Convert the input list of words to a set called word_set for faster lookup.
* Loop through each word in the input list.
* Loop through all possible prefixes and suffixes of the current word.
* Check if both the prefix and suffix are present in the input list (using word_set).
* If both the prefix and suffix are present, add the current word to the compound_words list and break out of the inner loop.
* Return the compound_words list.
* Call the find_compound_words() function with the words list as an argument.
* Print the returned list.
