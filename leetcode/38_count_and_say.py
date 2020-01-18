'''The count-and-say sequence is the sequence of integers with the first
five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-
-say sequence. You can do so recursively, in other words from the previous
member read off the digits, counting the number of digits in groups of the
same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and
"1", "2" can be read as "12" which means frequency = 1 and value = 2, the
same way "1" is read as "11", so the answer is the concatenation of "12"
and "11" which is "1211".
'''

import pytest

@pytest.mark.parametrize('input_and_output', [
    (4, "1211"),
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (5, "111221"),
    (6, "312211"),
    (7, "13112221")])
def test_count_and_say(input_and_output):
    input_natural = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = countAndSay(input_natural)
    assert expected_output == predicted_output


def countAndSay(n: int) -> str:
    ''' Iterative approach with memoization '''
    count_say_list = ["1"]
    for i in range(1, n):
        last_word = count_say_list[i-1]
        ''' Look at the last count and say word '''
        count_repeated = 0
        last_letter = last_word[0]
        next_word = ""
        for character in last_word:
            ''' Then we count how many letter are repetead '''
            if character == last_letter:
                count_repeated += 1
            else:
                ''' if the letter change, then we add how many
                    times the last letter was count with it
                    then reset the count '''
                next_word += str(count_repeated) + last_letter
                last_letter = character
                count_repeated = 1
        next_word += str(count_repeated) + last_letter
        ''' The last time is needed so we can store the last repetition '''
        count_say_list.append(next_word)
    return count_say_list[n-1]
        
