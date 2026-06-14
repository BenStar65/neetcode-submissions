class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number = []
        dictionary = {}
        length = []

        for numbers in nums:
            if numbers in dictionary:
                dictionary[numbers] += 1
            else:
                dictionary[numbers] = 1
        
        for index in dictionary:
            number.append(index)

        num_set = set(number)
        max_length = 0

        for num in num_set:
            
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                max_length = max(max_length, current_length)
        return max_length
        