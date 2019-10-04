import re
def fun(s):
    # return True if s is a valid email, else return False

    try:
        s = input("enter eth email")
        l = s.split('@')
        a = l[1].split('.')
        l.pop()
        l.append(a[0])
        l.append(a[1])
        if re.search('@', s) or re.search('.', s):
            if len(l) == 3 and len(l[2]) <= 3 and (
                    re.search('[a-z]', l[0]) or re.search('[A-Z]', l[0]) or not re.search('[_-]', l[0])):
                return (True)
    except IndexError:
        return (False)


def filter_mail(emails):
    return filter(fun, emails)


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print (filtered_emails)