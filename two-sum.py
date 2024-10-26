lst = [2, 5, 5, 11]
tagt = 10


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for index_first_iterable, i in enumerate(nums):
        for index_second_iterable, j in enumerate(nums):
            if (i + j) == target:
                if index_first_iterable == index_second_iterable:
                    continue
                return [index_first_iterable, index_second_iterable]


print(twoSum(lst, tagt))
