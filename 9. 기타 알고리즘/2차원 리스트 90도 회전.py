'''
2차원 리스트 90도 회전
ex) 
(0,0) (0,1) (0,2) (0,3) .. (0,M-1) 이 있다 가정했을 때 
--> 90도 회전 후 
(0,M-1) (1,M-1) (2,M-1) (2,M-1)

(p,q) -> (q,n-p-1)

'''

def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산 -> 세로 길이
    m = len(a[1]) # 열 길이 계산 -> 가로 길이
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

a = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]

print(len(a))
