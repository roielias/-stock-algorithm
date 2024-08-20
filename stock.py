#Calculate the number of consecutive days including today where the stock price is less than or equal to today's price.
def calculate_stock(prices):
    span = [0] * len(prices)
    for i in range(len(prices)):
        span[i] = 1  
        j = i - 1
        while j >= 0 and prices[j] <= prices[i]:
            span[i] += 1
            j -= 1
    return span

# efficiently Calculate the number of consecutive days including today where the stock price is less than or equal to today's price.
def stock_span(prices):
    span = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]        
        stack.append(i)
    return span


