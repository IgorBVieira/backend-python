def execute(x):
    fibonacci = (lambda x, x_1=1, x_2=0: 
    x_2 if x == 0
    else fibonacci(x - 1, x_1 + x_2, x_1))
    return fibonacci(x)

if __name__=='__main__':
    print(execute(5))
