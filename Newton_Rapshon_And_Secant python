def func(f, x):
    sum = 0
    temp = 0
    for i in range(len(f)):
        sum += f[i] * (x**(len(f)-1-temp))
        temp += 1

    return sum

def newton_raphson(f, df, x0, tol):
     while True:
        
        x_new = x0 - func(f, x0) / func(df, x0)

       
        relative_error = abs((x_new - x0) / x_new) * 100

       
        if relative_error < tol:
            return x_new

        
        x0 = x_new


result_newton = newton_raphson(f, df, 5, 0.00001)
print("Newton-Raphson Result:", result_newton)
print("Function Value at Result:", func(f, result_newton))

def secant(f, x_current, x_prev, tol):
   

    while True:
       
        x_next = x_current - (func(f, x_current) * (x_current - x_prev)) / (func(f, x_current) - func(f, x_prev))

        
        relative_error = abs((x_next - x_current) / x_next) * 100

       
        if relative_error < tol:
            return x_next

        
        x_prev = x_current
        x_current = x_next


result_secant = secant(f, 5, 7, 0.00001)
print("\nSecant Result:", result_secant)
print("Function Value at Result:", func(f, result_secant))
