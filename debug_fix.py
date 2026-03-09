# debug_fix.py
# Day 9 AM - Debug Problem: Modifying a list while iterating

# ─────────────────────────────────────────
# BUGGY CODE
# ─────────────────────────────────────────
nums = [1, 2, 3, 4, 5, 6, 7, 8]

for num in nums:
    if num % 2 == 0:
        nums.remove(num)

print("Buggy result :", nums)  # [1, 3, 5, 7, 6, 8] ← WRONG 

# ─────────────────────────────────────────
# WHY THE BUG HAPPENS
# ─────────────────────────────────────────
"""
When you remove an element while iterating, Python shifts all
remaining elements left by 1 index. The iterator's internal
pointer then SKIPS the next element.

Step-by-step with [2, 4, 6, 8]:
  - i=0: sees 2 → removes it → list becomes [4,6,8] → pointer moves to i=1
  - i=1: sees 6 (SKIPPED 4!) → removes it → list becomes [4,8]
  - i=2: out of range → loop stops
  - Result: [4, 8] — NOT empty as expected 

Rule: NEVER add or remove items from a list while iterating over it.
"""

# ─────────────────────────────────────────
# CORRECT SOLUTION — list comprehension
# ─────────────────────────────────────────
nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums = [n for n in nums if n % 2 != 0]  # keep only odd numbers
print("Fixed result :", nums)           # [1, 3, 5, 7] 

# ─────────────────────────────────────────
# Verify with the tricky case [2,4,6,8]
# ─────────────────────────────────────────
evens = [2, 4, 6, 8]
evens = [n for n in evens if n % 2 != 0]
print("All evens removed:", evens)      # [] 
