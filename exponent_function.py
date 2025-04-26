def raise_to_pow(number,pow_no):
    result = 1
    for i in range(pow_no):
        result= result*number
    return result

print(raise_to_pow(2,3))


result_simple = (2**3)
print(result_simple)


def pows(n1,n2):
    return n1**n2

print(pows(2,3))