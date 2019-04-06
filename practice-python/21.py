if __name__ == '__main__':
    N = int(input())
    L = []
    for item in range(N):
        nums = input().split()
        if nums[0] == 'insert':
            L.insert(int(nums[1]), int(nums[2]))
        elif nums[0] == 'print':
            print(L)
        elif nums[0] == 'remove':
            L.remove(int(nums[1]))
        elif nums[0] == 'append':
            L.append(int(nums[1]))
        elif nums[0] == 'sort':
            L.sort()
        elif nums[0] == 'pop':
            L.pop()
        elif nums[0] == 'reverse':
            L.reverse()
        else:
            print(L)

