# find remainder without using modulus
def divide(dividend, divisor):
    # if divisor == 0:
    #     return "Error: Divisor cannot be zero"
    negative = (dividend < 0) ^ (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    if negative:
        quotient = -quotient

    return quotient

dividend = -11
divisor = 2
result = divide(dividend, divisor)
print(result)