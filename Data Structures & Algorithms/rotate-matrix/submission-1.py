class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length=len(matrix)
        for i in range(len(matrix)//2):
            arr=matrix[length-i-1]
            matrix[length-1-i]=matrix[i]
            matrix[i]=arr
        print(matrix)
        for i in range(len(matrix)):
            for j in range(0,i):
                
                repl=matrix[j][i]
                matrix[j][i]=matrix[i][j]
                matrix[i][j]=repl
        print(matrix)
