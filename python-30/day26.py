# Enter your code here. Read input from STDIN. Print output to STDOUT

ad, am, ay = [int(x) for x in input().strip().split()] #actual return date
ed, em, ey = [int(x) for x in input().strip().split()] #expected return date

if (ay, am, ad) <= (ey, em, ed):
    print(0)
elif (ay, am) == (ey, em):
    print(15 * (ad - ed))
elif ay == ey:
    print(500 * (am - em))
else:
    print(10000)