import re

def count_substring(string, sub_string):
    substring = '(?='+sub_string+')' 
    count = len(re.findall(substring, string))
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)