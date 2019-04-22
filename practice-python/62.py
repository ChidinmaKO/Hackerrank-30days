# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
# n is an odd natural number
on = n//2

# for each index, multiply ".|." with 2 * the index and increment it. Center it and fill the sides with "-"
p = [(".|." * (2*i + 1)).center(m, "-")  for i in range(on)]

# next is the design. concatenate the pattern with "welcome" (centered with "-" at the sides) and reverse the entire pattern.
# Join with '\n' 

design = '\n'.join(p + ["WELCOME".center(m, "-")] + p[::-1])
print(design)