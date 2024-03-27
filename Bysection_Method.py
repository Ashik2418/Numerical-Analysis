def func(x, f):
    result = 0
    start = len(f) - 1
    for i in range(len(f)):
        result += f[start] * (x**i)
        start -= 1
    return result

def bisection_method(f, xl, xu, epsilon):
    rae = []
    iteration = []
    flag = 0
    
   
    def func_bisection(x):
        return func(x, f)

    
    if func_bisection(xl) * func_bisection(xu) > 0:
        print("Initial guesses do not have different signs.")
        return None

    while True:
        xr = (xl + xu) / 2.0
        rae.append(abs((xl - xu) / xr) * 100)
        iteration.append(flag)

        if func_bisection(xl) * func_bisection(xr) < 0:
            xu = xr
        else:
            xl = xr

        if rae[flag] < epsilon or flag == 1000:
            break

        flag += 1

    return xr, rae, iteration

f = [1, -2, 0, 4]
xl = 0
xu = 2
epsilon = 0.0001

result, relative_errors, iterations = bisection_method(f, xl, xu, epsilon)
print("Root:", result)
print("Function Value at Root:", func(result, f))
print("Relative Errors:", relative_errors)
print("Iterations:", iterations)
