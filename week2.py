import timeit

def main():
    matrixMatrix = []
    def makeMatrix(x, y):
        if x <= 0 or x <= 0 or y >= 500000 or y >= 500000:
            print("YOU SHALL NOT PASS")
            return 0
        else:
            for i in range(x):
                matrixMatrix.append([i + 1])
                for j in range(y - 1):
                    matrixMatrix[i].append((j + 2) * (i + 1))

            return matrixMatrix

    print("Time the matrix 5x5")
    start = timeit.default_timer()
    testcreate3 = makeMatrix(5, 5)
    stop = timeit.default_timer()
    print stop - start

    print("Time the matrix 10x10")
    start2 = timeit.default_timer()
    testcreate4 = makeMatrix(10, 10)
    stop2 = timeit.default_timer()
    print stop2 - start2

    print("Time the matrix 20x20")
    start3 = timeit.default_timer()
    testcreate5 = makeMatrix(20, 20)
    stop3 = timeit.default_timer()
    print stop3 - start3

    print("Time the matrix 50x50")
    start4 = timeit.default_timer()
    testcreate6 = makeMatrix(50, 50)
    stop4 = timeit.default_timer()
    print stop4 - start4

    print("Time the matrix 100x100")
    start5 = timeit.default_timer()
    testcreate7 = makeMatrix(100, 100)
    stop5 = timeit.default_timer()
    print stop5 - start5

    print("Time the matrix 250x250")
    start6 = timeit.default_timer()
    testcreate8 = makeMatrix(250, 250)
    stop6 = timeit.default_timer()
    print stop6 - start6


    if __name__ == '__main__':
        main()
