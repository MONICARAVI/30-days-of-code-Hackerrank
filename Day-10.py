
if __name__ == '__main__':
    n = int(input())

    count1 = 0
    maxcount = 0

    while(n>0):
        if(n%2):
            count1 += 1
            if(count1>maxcount):
                maxcount = count1
        else:
            count1 = 0
        n = n//2
    print(maxcount)

