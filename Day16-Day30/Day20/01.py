

def reversed_cmp(x,y):
    if x > y:
        return -1
    if x < y:
        return 0

print(sorted([36,5,23,21],reversed_cmp))


def cmp_ignore_case(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    
    if s1 < s2:
        return -1
    if s1 == s2:
        return 0
    if s1 > s2:
        return 1

print(list(sorted(['bob','about','Zoo','Credit'],cmp_ignore_case)))
