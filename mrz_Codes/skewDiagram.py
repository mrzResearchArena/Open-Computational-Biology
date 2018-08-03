X = ['TTTTGGAGCGATCGATTG']
Y = [-1]

import matplotlib.pyplot as plt
import numpy as np

# import readXY
# X, Y = readXY.fetchXY()

def skewDiagram(x):
    value = 0
    valueMaxMin = []
    for base in x:
        if base == 'C':
            value -= 1
            valueMaxMin.append(value)

        else:
            if base == 'G':
                value += 1
                valueMaxMin.append(value)

            else:
                value += 0
                valueMaxMin.append(value)

    plt.plot(range(0, len(valueMaxMin)), np.array(valueMaxMin))
    # plt.grid(False)
    # plt.grid(linestyle='-', color='red')
    # plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='.75', color='black')
    plt.minorticks_on()
    plt.xlabel('Position in Sequence')
    plt.ylabel('Cumulative GC Skew')
    plt.show()

    return value, max(valueMaxMin), min(valueMaxMin)

def GCContent(x):
    A = x.count('A'); C = x.count('C'); G = x.count('G'); T = x.count('T')
    return ((G+C) / (A+C+G+T))*100.0

if __name__ == '__main__':
    for x, y in zip(X, Y):
        v = skewDiagram(x) # (value, max, min)
        print(v)
