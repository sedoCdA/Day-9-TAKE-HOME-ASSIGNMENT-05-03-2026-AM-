# rotate_list.py
# Day 9 AM - List Rotation using Slicing

# ─────────────────────────────────────────
# rotate_list function
# ─────────────────────────────────────────
def rotate_list(lst, k):
    """
    Rotates list to the RIGHT by k positions using slicing.
    Handles k > len(lst) using modulo.

    Example:
        rotate_list([1,2,3,4,5], 2) → [4,5,1,2,3]

    How slicing works here:
        lst[-k:]  → last k elements  → [4,5]
        lst[:-k]  → remaining elements → [1,2,3]
        combined  → [4,5,1,2,3]
    """
    if not lst:
        return lst
    k = k % len(lst)       # handles k > len(lst)
    return lst[-k:] + lst[:-k]

# ─────────────────────────────────────────
# Tests
# ─────────────────────────────────────────
if __name__ == "__main__":
    print(rotate_list([1, 2, 3, 4, 5], 2))  # [4,5,1,2,3] 
    print(rotate_list([1, 2, 3, 4, 5], 7))  # [4,5,1,2,3] — k > len 
    print(rotate_list([1, 2, 3, 4, 5], 0))  # [1,2,3,4,5] — no rotation
    print(rotate_list([], 3))               # []           — empty list
