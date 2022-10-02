#Opcion1
def op1():
    for i in range(0,11):
        print(f'{i}**2 {i**2}')


#Opcion2
squares = []
def op2():
    for i in range(0,101):
        if i % 3 != 0: #De los que no son divisibles entre tres
            squares.append(i**2)
    print(squares)


def op3():
    for i in range(0,11):
        if i % 3 == 0: # De los que son divisibles entre tres
            print(f'{i}**2 {i**2}')

def lc():
    sqr = []
    sqr = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(sqr)

def reto():
    lst = []
    lst = [i**2 for i in range(1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(lst)

if __name__ == '__main__':
    op2()