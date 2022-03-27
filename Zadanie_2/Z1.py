print(f'Type number')
arg1 = int(input())
lambda_fun = lambda x: x + 15
print(f'lambda 1 {lambda_fun(arg1)}')
print(f'Type number')
arg2 = int(input())
lambda_fun2 = lambda y: arg1*y
print(f'lambda 2 {lambda_fun2(arg2)}')