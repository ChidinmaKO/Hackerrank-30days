# Using regex 1

import re
def fun(s):
    # return True if s is a valid email, else return False
    regex_pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{0,3}$'
    return (bool(re.match(regex_pattern, s)))
    
# Using regex 2
def fun(s):
    # return True if s is a valid email, else return False
    if(re.search(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$',s)) != None:
        return True
    else:
        return False

# Using exceptions, map, lambda & all
def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, url = s.split('@')
        websitename, extension = url.split('.')
        if any([username == '', url == '', websitename == '', extension == '']):
            return False
    except ValueError:
        return False
    
    # check that the username only contain letters, digits, dashes and underscores.
    first = all(map(lambda x: x.isdigit() or x.islower() or x.isupper() or x == '_' or x == '-', username))

    # check that the website name only contains letters and digits
    second = all(map(lambda x: x.isdigit() or x.islower() or x.isupper(), websitename))

    # check that the extension has a maximum length of 3
    third = 0 < len(extension) < 4

    return all([first, second, third])

    



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)