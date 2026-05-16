from sys import exit


def get_columns(matrix):
    columns = []
    for i in range(0, len(matrix)):
        for v in range(0, len(matrix[i])):
            try:
                columns[v].append(matrix[i][v])
            except:
                columns.append([])
                columns[v].append(matrix[i][v])
    return columns


def multiply_matrix(matrix1, matrix2):
    if len(get_columns(matrix1)) != len(matrix2):
        print(f"Matrix 2: {matrix2}")
        print(f"{len(get_columns(matrix1))} - {len(matrix2)}")
        print("num of columns in matrix 1 is not equal to num of rows in matrix 2!")
        exit()
    else:
        rows1 = matrix1
        cols2 = get_columns(matrix2)
        new_matrix = []
        for i in range(0, len(cols2)):
            for j in range(0, len(rows1)):
                ans = 0
                for k in range(0, len(rows1[j])):
                    ans += cols2[i][k] * rows1[j][k]
                try:
                    new_matrix[j].append(ans)
                except:
                    new_matrix.append([])
                    new_matrix[j].append(ans)
        return new_matrix


if __name__ == '__main__':
    matrix1 = [
        [-1.0, -1.0, -1.0, 1.0]
    ]
    matrix2 = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, -5],
        [0, 0, 0, 1]
    ]

    m = multiply_matrix(matrix1, matrix2)
    for i in range(len(m)):
        print(m[i])
