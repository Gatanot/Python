def show_magicians(lists):
    for list in lists:
        print(list)

magicians = ['a','b','c','d']

show_magicians(magicians)

def make_magicians(lists):
    a=len(lists)
    b = 0
    c = []
    while b < a:
        for list in lists:
            c.append("the Great " + list)
            b = b + 1
    return c

print(make_magicians(magicians),magicians)
