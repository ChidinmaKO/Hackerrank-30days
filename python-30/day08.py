# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
# split the name and the number
name_num = [input().split() for _ in range(n)]
# the phone number dictionary
phone_dict = {k: v for k,v in name_num}
while True:
    try:
        name = str(input())
        if name in phone_dict:
            print("{}={}".format(name, phone_dict[name]))
        else:
            print("Not found")
    except:
        break
