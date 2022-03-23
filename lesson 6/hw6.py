def get_list() -> list:
    return list(range(0, 1_000_000_000, 2))

class Solution:


    def find_target(self, list, target):
        left = 0
        right = len(list)
        step = 0
        while left <= right:
            step += 1
            middle_index = (left + right) // 2
            if list[middle_index] < target:
                left = middle_index + 1
            elif list[middle_index] > target:
                right = middle_index - 1
            else:
                return step


print(Solution().find_target(get_list(), 616378))