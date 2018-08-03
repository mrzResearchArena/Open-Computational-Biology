def main():

    with open('/home/rafsanjani/Downloads/rosalind_bins(1).txt', 'r') as File:
        _, _, A1, A2 = [line.strip().split('\n') for line in File.readlines()]
        A1 = [int(i) for i in A1[0].split()]
        A2 = [int(i) for i in A2[0].split()]


    d = {}
    C=1
    for i in A1:
        d[i] = C
        C += 1


    for i in A2:
        try:
            print(d[i], end=' ')
        except:
            print(-1, end=' ')


if __name__ == '__main__':
    main()
