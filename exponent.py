# print(2**3) # ** is exponent

# function to do exponent manually using for loop
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

# call of result that stores the raise_to_power answer
print(raise_to_power(3,4))