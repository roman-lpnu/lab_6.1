import random

def sum(b,i,s):
    if i<len(b)-1:
        if not (b[i]%2!=0  and b[i]%3==0):
            s += b[i]
            return sum(b,i+1,s)
        else:
            return sum(b,i+1,s)
    else:
        return s

def create(b,low,high,i):
    if i<20:
        b.append(random.randint(low,high))
        create(b,low,high,i+1)

def filter(b,i):
    if i==len(b):
        return b
    if not (b[i]%2!=0  and b[i]%3==0):
        b[i] = 0
        return filter(b, i + 1)
    if i < len(b)-1:
        return filter(b, i + 1)


def main():
    b=[]
    create(b,10,90,0)
    print(b)
    print('Sum=' + str(sum(b, 0, 0)))
    filter(b,0)
    print(b)


if __name__=='__main__':
    main()
