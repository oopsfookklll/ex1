```python
from itertools import combinations

def min_abs_diff(nums):
    n = len(nums) // 2
    total_sum = sum(nums)
    min_diff = float('inf')

    for comb in combinations(nums, n):
        sum_comb = sum(comb)
        other_sum = total_sum - sum_comb
        diff = abs(sum_comb - other_sum)
        min_diff = min(min_diff, diff)

    return min_diff
```