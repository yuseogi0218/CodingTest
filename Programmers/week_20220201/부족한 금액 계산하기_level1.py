def solution(price, money, count):
    total_price = 0

    for i in range(count):
        total_price += price * (i + 1)

    result = total_price - money

    if result < 0:
        return 0
    else:
        return result


solution(3, 20, 4)
