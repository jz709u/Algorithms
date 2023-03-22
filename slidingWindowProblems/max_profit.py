## Naive Approach
## for each bought day loop over every day after the bought day
## Performance O(n log n)
## Space: O(1)

## Optimized Approach
## window approach buy first sell each viable day and save profit if it's
## better than the current best profit until it reaches end of array or
## profit is negative then buy that day and repeat above
## Performance: O(n)
## Space: O(1)
def max_profit(stock_prices): 
    maxProfit = 0 
    if len(stock_prices) <= 1:
        return maxProfit
    
    buyDay = 0
    for currentDay in range(1, len(stock_prices)):
        result = stock_prices[currentDay] - stock_prices[buyDay]
        if result >= 0:
            maxProfit = max(maxProfit, result)
        else:
            buyDay = currentDay
    
    return maxProfit