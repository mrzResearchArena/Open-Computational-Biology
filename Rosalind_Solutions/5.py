
def main():

    n=6
    from itertools import permutations
    P = list(permutations(range(1, n+1)))

    print(len(P))
    for i in P:
        # print('{} {} {}'.format(i[0], i[1], i[2]))
        for C in range(n):
            print('{}'.format(i[C]), end=' ')
        print()


if __name__ == '__main__':
    main()
    
