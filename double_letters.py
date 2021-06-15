# double letter solution
def double_letters(string):
    lst=[]
    for i in string:
        lst.append(i)
    x=0
    while x < len(lst) - 1:
        if lst[x] == lst[x+1]:
            return True
        x=x+1
    return False

def find_double_letters3(word):
    return len([x for x in word if x*2 in word]) >= 1
print(find_double_letters3('nono'))
print(find_double_letters3('hello'))
print(find_double_letters3('racecar'))
