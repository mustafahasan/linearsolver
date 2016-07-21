import numpy as np
import sys

def genMatrix(datalines, d, bVector):
    newMatrix = []

    for x in range(0,d):
        dataline = datalines.readline().split()
        yVals = list(map(float, dataline))
        yVals.append(bVector[x])
        newMatrix.append(yVals)

    return newMatrix

def gaus(primeA, n):

    for i in range(0, n - 1):
        pivotR = i

        for j in range(i + 1, n):
            if(abs(primeA[i][j]) > abs(primeA[pivotR][i])):
                pivotR = j

            primeA[[pivotR, i ]] = primeA[[i, pivotR]]

        for j in range(i + 1, n):
            t = (primeA[j][i])/(primeA[i][i])

            for k in range(i, n + 1):
                primeA[j][k] = (primeA[j][k]) - (primeA[i][k] * t)

    return primeA

def backtrack(matrix, n):
    solVector = list([0] * n)
    finalVector = list()

    for i in reversed(range(n)):
        t = (matrix[i][n])
        for j in range(i + 1, n):
            t = (t - (solVector[j] * matrix[i][j]))

        solVector[i] = float(t/(matrix[i][i]))

    for x in solVector:
        k = format(x, '0.3f')
        finalVector.append(float(k))

    return finalVector

arg1 = sys.argv[1]
aFile = open(arg1, 'r+')
bFile = open(arg1, 'r+')

n = int(aFile.readline())
lines = bFile.readlines()
lastLine = lines[n+1].split()
bVector = list(map(float, lastLine))

matrix = genMatrix(aFile, n, bVector)
matrix = np.array(matrix)
matrix = gaus(matrix, n)

for i in range(0, n):
    counter = 0
    for j in range(0, n + 1):
        if (float(matrix[i][j]) == 0):
            counter += 1

        if (counter == (n + 1)):
                print("Exiting....... The system is indeterminate.")
                exit()

        if (counter == n and float(matrix[i][n]) != 0):
            print("Exiting....... The system is inconsistent.")
            exit()

solVector = backtrack(matrix, n)

print(solVector)