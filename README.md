# Algorithimc-Thinking-Python-Solutions
This repository contains solutions to all the tasks presented in the book "Algorithmic Thinking" by Daniel Zingaro in Python

Link: https://www.amazon.com/Algorithmic-Thinking-Problem-Based-Daniel-Zingaro-ebook/dp/B085BVJ51Z?ref_=ast_author_dp

## Snowflakes Code description 
In summary, this code takes a list of snowflakes as input, and checks if there are any duplicate snowflakes. If duplicates are found, it returns the total number of equal lists and the lists that have a pair.

###### Steps:

* Initialize the class with the given snowflakes list, an empty dictionary to store the count of equal lists, and an empty list to store the equal lists.
* Define a method called sorted_snowflakes that sorts each snowflake in the list of snowflakes in ascending order and returns a new list containing the sorted snowflakes.
* Define a method called count_equal_lists that calls the sorted_snowflakes method to get the sorted snowflakes list and loops through the sorted snowflakes to compare each pair of snowflakes. If two snowflakes are equal, the method checks if the sorted snowflake is already in the count_snowflakes dictionary. If it's not, it adds the snowflake to the dictionary with a count of 1 and adds the snowflake to the same_list. If the sorted snowflake is already in the dictionary, it increments the count of the snowflake in the dictionary.
* Define a method called print_results that calls the count_equal_lists method to count the number of equal lists and print the result. The method also prints the snowflakes that have a pair (i.e., the snowflakes that occur more than once in the original list).

## CompoundWords Code description 

This code defines a function called find_compound_words() which takes in a list of words as an argument, and returns a list of all the compound words in the input list. A compound word is a word that can be formed by concatenating two or more smaller words that are also present in the input list.

The function loops through each word in the input list, and then loops through all the possible prefixes and suffixes of that word. It checks whether both the prefix and suffix are present in the input list, and if so, adds the current word to a list of compound words.

The function then returns the list of compound words.

###### Steps:

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

## WritingCheck Code Description 

The code defines two strings s1 and s2, and s2 has one letter less than s1. There is function writing_check that checks how many ways s1 can be transformed into s2 by removing a single character. It also defines a main function that calls writing_check with s1 and s2 and prints a message indicating the number of possible ways to transform s1 into s2. The code is intended to demonstrate a simple string manipulation problem.

###### Steps:

* Define two strings s1 and s2 with some differences.
* Define a function writing_check that takes two strings, invalid and valid, as input.
* Initialize a counter variable count to 0.
* Iterate over each character in invalid.
* Check if the invalid string with the ith character removed is equal to valid.
* If so, increment the count variable.
* Return the count variable.
* Define a main function that calls writing_check with s1 and s2.
* Depending on the output of writing_check, print a message that indicates the number of possible ways to transform s1 into s2.
