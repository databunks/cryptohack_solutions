

def matrix2List(matrix):
    a = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            a.append(matrix[i][j])
    return a


def add_round_key(s, k):
    s = matrix2List(s)
    k = matrix2List(k)
    res = []

    for i in range(0, len(s)):
        res.append(s[i] ^ k[i])

    return bytes(res)

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


    


print(add_round_key(state, round_key))

