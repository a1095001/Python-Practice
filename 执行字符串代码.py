func = """ 
def factorial(number):
    if number < 1:
        return False
    elif number == 1:
        return 1
    else:
        return number * factorial(number - 1)
"""
exec(func)
a = factorial(5)
print(a)