# Task 1
def filter_list(some_list):
    return [x for x in some_list if type(x) != str]


# Task 2
def first_non_repeating_letter(my_str):
    lpstr = my_str.lower()
    for i in range(len(lpstr)):
        if lpstr.count(lpstr[i]) == 1:
            return my_str[i]
    return ""


# Task 3
def digital_root(n):
    while n > 9:
        n = sum(int(x) for x in str(n))
    return n


# Task 4
def number_of_pairs(my_str):
    n = 0
    for i in range(len(my_str)):
        for j in range(i + 1, len(my_str)):
            if my_str[i] + my_str[j] == 5:
                n += 1
    return n


# Task 5
def take_second(elem):
    return elem[1]


def take_first(elem):
    return elem[0]


def sort_friend(some_string):
    s1 = some_string.upper().split(';')
    s2 = []
    for i in range(len(s1)):
        s2.append(s1[i].split(':'))
        s2[i].reverse()
    s2.sort(key=take_second)
    s2.sort(key=take_first)
    result = ''
    for i in range(len(s2)):
        result = result + '(' + s2[i][0] + ', ' + s2[i][1] + ') '
    return result


a = filter_list([2, 3, 'qwerty', 4])
print(a)
b = first_non_repeating_letter('sTreSS')
print(b)
c = digital_root(12345)
print(c)
d = number_of_pairs([1, 3, 6, 2, 2, 0, 4, 5])
print(d)
e = sort_friend('Fired:Corwill;Wilfred:Corwill;Barney:TornBull;'
                'Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill')
print(e)

