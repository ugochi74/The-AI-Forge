
def matrix_rank(matrix):
    rows = len(matrix)

    if rows == 0:
        raise ValueError("Matrix cannot be empty")

    columns = len(matrix[0])

    if columns == 0:
        raise ValueError("Matrix cannot have empty rows")

    for row in matrix:
        if len(row) != columns:
            raise ValueError("All rows must have the same length")

    # Create a copy so we do not modify the original matrix.
    result = [row[:] for row in matrix]

    pivot_row = 0
    rank = 0

    for column in range(columns):

        # Find a non-zero pivot.
        selected_row = None

        for row in range(pivot_row, rows):
            if abs(result[row][column]) > 1e-10:
                selected_row = row
                break

        if selected_row is None:
            continue

        # Move the selected row into the pivot position.
        result[pivot_row], result[selected_row] = (
            result[selected_row],
            result[pivot_row]
        )

        # Make the pivot equal to 1.
        pivot = result[pivot_row][column]

        for j in range(column, columns):
            result[pivot_row][j] /= pivot

        # Eliminate values below the pivot.
        for row in range(pivot_row + 1, rows):
            factor = result[row][column]

            for j in range(column, columns):
                result[row][j] -= factor * result[pivot_row][j]

        rank += 1
        pivot_row += 1

        if pivot_row == rows:
            break

    return rank


if __name__ == "__main__":
    matrix = [
        [1, 0, 2],
        [0, 1, 1],
        [2, 1, 5]
    ]

    print("Matrix rank:", matrix_rank(matrix))
