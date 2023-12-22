def p_number(num):
    result = 0
    gg = 1
    for i in range(num):
        print(gg)
        gg += 1
        result += gg
    return result

# Приклад використання:
x = 4  # Значення p
result = p_number(x)
print(result)
# 1+ 3+ 6 + 10 + 15
#  +2 +3 + 4 + 5