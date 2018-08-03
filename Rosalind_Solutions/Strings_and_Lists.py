
def main():

    a, b, c, d =22, 27, 97, 102

    s='HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain'
    seq1 = ''
    seq2 = ''
    for n, i in enumerate(s):
        if a<=n<=b:
            seq1 += i

        if c<=n<=d:
            seq2 += i

    print(seq1)
    print(seq2)


if __name__ == '__main__':
    main()
