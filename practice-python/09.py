if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = sorted(set(arr))[-2]
    print(a)