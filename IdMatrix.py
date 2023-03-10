class IdentityMatrix:
    def id_mtrx(n):
        try:
            neg = False
            if n < 0: 
                n*=-1
                neg = True
            matrix = [[0 for _ in range(n)] for _ in range(n)]
            if not neg:
                for i in range(n):
                    matrix[i][i] = 1
            else:
                for i in range(1, n+1):
                    matrix[i-1][n-i] = 1
            return matrix
        except:
            return "Error"  
        
