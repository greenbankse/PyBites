def fizzbuzz(num):
    return (
        "Fizz Buzz"
        if num % (3 * 5) == 0
        else "Fizz"
        if num % 3 == 0
        else "Buzz"
        if num % 5 == 0
        else num
    )


L = [fizzbuzz(n) for n in range(1, 20)]

print(L)


# # Pybites solution
# def fizzbuzz(num):
#     if (num % (5*3)) == 0:
#         r = "Fizz Buzz"
#     elif (num % 5) == 0:
#         r = "Buzz"
#     elif (num % 3) == 0:
#         r = "Fizz"
#     else:
#         r = num
#     return r
