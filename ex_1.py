def p_number(num):
    result = 0
    gg = 1
    sum = 0
    for i in range(num):
        result += gg
        gg += 1
        print(result)
        sum += result
    return sum
x = 5  
result = p_number(x)
print(result)
