def fibonacci(n, k):
    a, b=1, 1
    for _ in range(3,n+1):
        a,b=b,k*a+b
        print(b)



if __name__ == '__main__':
    # main()
    v=fibonacci(5, 3)
    print(v)
    
