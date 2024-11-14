# # factorial calculation using recursive function
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5)) # 120
# do this without gthe recursive function
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
factorial(5) # 120