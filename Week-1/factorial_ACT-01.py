# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# def main():
#     number = int(input("Enter a non-negative integer: "))
#     if number < 0:
#         print("Factorial is not defined for negative numbers.")
#     else:
#         result = factorial(number)
#         print(f"The factorial of {number} is {result}")

def factorial():
    number = input("input value(PlEASE PUT INTERGER NUMBER): ")
    n = int(number)
    if n < 0:
        return "Undefined for negative numbers"
    elif 0 <= n <= 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            print("Current value of i:", i)
            result *= i
        return result


if __name__ == "__main__":
    ans = factorial()
    print("\n the final results: ", ans)