# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for _ in range(t):
    try:
        a,b = map(int, input().split())
        result = (a//b)
        print(result)
    except BaseException as e: 
        '''
        Note that 'except Exception as e:' works.
        Using base exception since it is the base class for all built-in exceptions.
        Note that it isn't directly inherited for user-defined exceptions... In that
        case use Exception instead of BaseException.
        '''
        print("Error Code:", e)