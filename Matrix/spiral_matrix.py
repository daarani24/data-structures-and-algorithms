def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
    return res

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix = []
   
    for i in range(rows):
        while True:
            row_input = input(f"Row {i+1}: ")
            row = list(map(int, row_input.split()))
            if len(row) == cols:
                matrix.append(row)
                break
    
    result = spiral_order(matrix)
    
    print("\nSpiral Order Traversal:")
    print(result)