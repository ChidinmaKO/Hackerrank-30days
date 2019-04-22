import string

def print_rangoli(size):
    a = string.ascii_lowercase
    width = (4*size - 3)
    r = []
    
    for i in range(size):
        s = '-'.join(a[i:size])
        r.append((s[::-1] + s[1:]).center(width, '-'))
        rangoli = '\n'.join(r[::-1] + r[1:])
    print(rangoli)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)