# RECUSIVE BINARY SEARCH
def binary_search(l: int, r: int, nums: list[int], target: int) -> int:
    if l > r:
        return -1
    m = l + (r - l) // 2

    if nums[m] == target:
        return m
    if nums[m] < target:
        return binary_search(m + 1, r, nums, target)
    return binary_search(l, m - 1, nums, target)


def search(nums: list[int], target: int) -> int:
    return binary_search(0, len(nums) - 1, nums, target)


res = search(nums=[1, 2, 3, 4, 5], target=3)
print(res)
