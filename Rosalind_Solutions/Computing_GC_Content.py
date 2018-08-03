def main():

    with open('/home/rafsanjani/Downloads/rosalind_gc(1).txt', 'r') as file:
        genome = ''
        for line in file:
            if line[0] == '>':
                names.append(line.strip()[1:])
                if len(genome)>0:
                    # print(gcContent(genome))
                    percentage.append(gcContent(genome))
                genome = ''
            else:
                genome += line.rstrip()

        percentage.append(gcContent(genome))

        # print(names)
        # print(percentage)


    d = dict(zip(names, percentage))
    # print(d)
    print(sorted(d.items(), key=lambda x:x[0]))



if __name__ == '__main__':
    main()
