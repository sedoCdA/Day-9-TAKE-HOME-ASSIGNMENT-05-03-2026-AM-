# matrix_ops.py
# Day 9 AM - Matrix Operations using nested lists

# ─────────────────────────────────────────
# 1. Matrix Addition
# ─────────────────────────────────────────
def matrix_add(A, B):
    """Returns element-wise sum of two matrices."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# ─────────────────────────────────────────
# 2. Matrix Transpose
# ─────────────────────────────────────────
def matrix_transpose(matrix):
    """Returns the transpose using zip(*matrix)."""
    return [list(row) for row in zip(*matrix)]

# ─────────────────────────────────────────
# 3. Matrix Multiplication
# ─────────────────────────────────────────
def matrix_multiply(A, B):
    """
    Returns dot product of A x B.
    Handles dimension mismatch gracefully.
    """
    if len(A[0]) != len(B):
        raise ValueError(
            f"Dimension mismatch: A has {len(A[0])} cols, B has {len(B)} rows."
        )
    return [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*B)]
        for row_a in A
    ]

# ─────────────────────────────────────────
# Tests
# ─────────────────────────────────────────
if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    print("Matrix A:", a)
    print("Matrix B:", b)

    print("\nAddition:")
    print(matrix_add(a, b))           # [[6,8],[10,12]]

    print("\nTranspose of A:")
    print(matrix_transpose(a))        # [[1,3],[2,4]]

    print("\nMultiplication:")
    print(matrix_multiply(a, b))      # [[19,22],[43,50]]

    # Test with 3x3
    c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    d = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    print("\n3x3 Addition:")
    print(matrix_add(c, d))

    print("\n3x3 Multiplication:")
    print(matrix_multiply(c, d))

    # Test dimension mismatch error handling
    try:
        matrix_multiply([[1, 2]], [[1, 2]])
    except ValueError as e:
        print(f"\nCaught error: {e}")
