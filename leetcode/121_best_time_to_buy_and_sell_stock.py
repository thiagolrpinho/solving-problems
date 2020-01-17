'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
import pytest
from typing import List

@pytest.mark.parametrize('input_and_output', [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
    ([2,4,1], 2)])
def test_max_profit(input_and_output):
    input_list = input_and_output[0]
    expected_output = input_and_output[1]
    predicted_output = maxProfit(input_list)
    assert expected_output == predicted_output


def maxProfit(prices: List[int]) -> int:
    best_price, profit = float('inf'), 0
    for price in prices:
        best_price, profit = min(best_price, price), max(profit, price-best_price)
    return profit
