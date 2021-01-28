"""
matrix = [
[-1,-2,1,5],
[-5,4,-1,2],
[-1,-4,-2,10],
[-1,-1,-2,0]]
"""
matrix = [
    [-7, 14,42],
    [-4,-6,36],
    [4,1,-4],
    [1,0,-1],
    [0,1,-0,5],
    [-14,-21,0]]

# Part 1
#Preperation of the matrix
def add_q_col_to_matrix(matrix):
    for x in matrix:
        x.append(0)
    return matrix

# 1st step, get the pivot column, return false if there isn't any. Meaning, it's finished
def get_pivot_column(z):
    pivot_val = min(z[0:len(z)-2:1])

    if(pivot_val < 0):
        return z.index(pivot_val)
    else:
        return False

# 2nd step calculate the q column, if the calculation is < 0.
def calculate_q(matrix, pivot_col):
    for x in matrix:
        try:
            q_value = round(x[-2] / x[pivot_col],2)
        except ArithmeticError:
            pass
        
        if(q_value < 0):
            x[-1] = q_value
            
    return matrix

# 3rd step calculate the pivot row
def get_pivot_row(matrix):
    q_column = []
    for x in matrix:
        q_column.append(x[-1])
        
    f =  [i for i in q_column if i != 0]
    return q_column.index(max(f))
#--------------------------------------------------------------------------------------------------------------
# Part 2
# 1st step Calculate the basement/new pivot row
def calculate_new_pivot_row(matrix, pivot_row, pivot_col):
    for x in range(len(matrix[pivot_row])-1):
        if x != pivot_col:
            matrix[pivot_row][x] = round(-1 * (matrix[pivot_row][x] / matrix[pivot_row][pivot_col]),2)
    return matrix[pivot_row]

# 2nd step calcualte remaining elements
def calcualte_remaining_elements(matrix, basement_row, pivot_row, pivot_col):

    for rows in matrix:
        if(matrix.index(rows) != pivot_row):
            for col_index in range(len(rows) - 1):
                if col_index != pivot_col:
                    rows[col_index] = round(rows[col_index] + rows[pivot_col] * basement_row[col_index],2)
                    
    return matrix

# 3rd step Calculate the new pivot column
def calculate_new_pivot_column(matrix, pivot_row, pivot_col):
    for x in matrix:
        if matrix.index(x) != pivot_row:
            x[pivot_col] = round(x[pivot_col] / matrix[pivot_row][pivot_col],2)
    return matrix

# 4th step calcualte the Pivot elment
def calculate_pivot_element(matrix, pivot_row, pivot_col):
    matrix[pivot_row][pivot_col] = round(1 / matrix[pivot_row][pivot_col],2)
    return matrix

# 5th step reset q
def reset_q(matrix):
    for x in matrix:
        x[-1] = 0
    return matrix


if __name__ == '__main__':
    # Preperation part
    # prepare Matrix
    matrix = add_q_col_to_matrix(matrix)
#--------------------------------------------------------------------------------------------------------------
    while(get_pivot_column(matrix[-1])):
        # (1st step) Calculate the pivot column
        pivot_col = get_pivot_column(matrix[-1])
        print("Pivot column = ", pivot_col)

        #(2nd step) Calculate the q column
        matrix = calculate_q(matrix, pivot_col)

         # (3rd step) Calculate the pivot row
        pivot_row = get_pivot_row(matrix)
        print("Pivot row = ", pivot_row)
    #--------------------------------------------------------------------------------------------------------------   
        # (1st step) Calcualte new pivot row
        basement_row = calculate_new_pivot_row(matrix, pivot_row, pivot_col)
        print("New Pivot Row = ", basement_row)

        # (2nd step) Calcualte remaining elements
        matrix = calcualte_remaining_elements(matrix, basement_row, pivot_row, pivot_col)
        print("Rest elements calculated = ", matrix)
        
        # (3rd step) Calculate new pivot column
        matrix = calculate_new_pivot_column(matrix, pivot_row, pivot_col)
        print("New Pivot Column = ", matrix)
            
        # (4th step) Calcualte the pivot element
        calculate_pivot_element(matrix, pivot_row, pivot_col)
        print("Pivot element calculated", matrix)

         # (5th step) reset q
        matrix = reset_q(matrix)
        print("Finalized Matrix interation = ", matrix)
        print("---"*10)
