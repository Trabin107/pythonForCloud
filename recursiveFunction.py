# # factorial calculation using recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5)) # 120
# print(factorial(5)) # 120
# do this without gthe recursive function
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(factorial(5)) # 120