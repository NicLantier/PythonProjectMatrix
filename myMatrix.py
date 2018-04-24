matrixmatrix = []

class myMatrix(object):
    def makeMatrix(rows, cols):
        if rows <= 0 or cols <= 0 or rows >= 500000 or cols >= 5000000:
            print("YOU SHALL NOT PASS")
            return 0
        else:
            for i in range(rows):
                matrixmatrix.append([i + 1])
                for j in range(cols - 1):
                    matrixmatrix[i].append((j + 2) * (i + 1))

    def matrixMultipy(matrixA, matrixB):
        matrixC = [[0 for col in range(len(matrixB[0]))] for row in range(len(matrixA))]
        for x in range(len(matrixA)):
            for y in range(len(matrixB[0])):
                for z in range(len(matrixB)):
                    matrixC[x][y] += matrixA[x][z] * matrixB[z][y]
        return matrixC

    def matrixScaling(scalar, matrix):
        matrixScaled = matrix

        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                matrixScaled[x][y] = scalar * matrix[x][y]
        return matrixScaled

    def matrixDivide(value, matrix):
        matrixdivided = matrix

        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                matrixdivided[x][y] = matrix[x][y] / value
        return matrixdivided

    def matrixExpScaling(value, matrix):
        matrixExpoScaled = matrix

        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                matrixExpoScaled[x][y] = matrixExpoScaled[x][y] ** value
        return matrixExpoScaled

    def matrixSum(matrix):
        matrixSum = 0

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                matrixSum += matrix[x][y]
        return matrixSum
    pass

def main():

    print("Test 3X5 matrix")
    testMatrix = myMatrix.makeMatrix(3, 5)
    print(testMatrix)

    print("Testing a 5X3 matrix")
    testMatrixX = myMatrix.makeMatrix(5, 3)
    print(testMatrixX)

    print("Multiplying the two above matrices")
    multiplyTest = myMatrix.matrixMultiply(testMatrix,testMatrixX)
    print(multiplyTest)

    print("Matrix")
    print(testMatrix)
    print("Scaling matrix by 3")
    scalingTest = myMatrix.matrixScaling(3, testMatrix)
    print(scalingTest)

    print("Matrix")
    print(testMatrixX)
    print("Dividing matrix by 4")
    divideTest = myMatrix.matrixDivide(4, testMatrixX)
    print(divideTest)

    print("Matrix")
    print (testMatrix)
    print("Exponitial scaling by 2")
    expoScalingTest = myMatrix.matrixExpScaling(2, testMatrix)
    print (expoScalingTest)

    print("Matrix")
    print testMatrix
    print("sum of the elements")
    sumMatrix = myMatrix.matrixSum(testMatrix)
    print sumMatrix


    if __name__ == '__main__':
        main()