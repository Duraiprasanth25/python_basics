import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " mil sec")
        return result

    return wrapper #first class argument

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)



def check(f):
    def helper(z):
        if type(z) == int and z > 0:
            return f(z)
        else:
            raise Exception("Argument is not a non_negative number")
    return helper
@check
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


for i in range(1, 10):
    print(i, factorial(i))

try:
    print(factorial(-1))
except Exception as e:
    print("Error: ", e)

try:
    print(factorial(1.354))
except Exception as e:
    print("Error: ", e)
