class MatrixAdjacency():
    # checks matrix to see if node1 is connected to node2 
    def is_adjacent(matrix, node1, node2):
        if matrix[node1][node2] == 1:
            return True
        else:
            return False


