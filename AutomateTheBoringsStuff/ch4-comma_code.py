def comma_code(lst):
    string = ''
    n = len(lst)
    for i in range(n):
        if i != n - 1:
            string += lst[i] + ', '
        else:
            string += 'and ' + lst[i]
    return string


spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))
