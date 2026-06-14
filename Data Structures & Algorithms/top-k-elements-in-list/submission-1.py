class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for index in nums:
            if index in dictionary:
                dictionary[index] += 1
            else:
                dictionary[index] = 1
        most_shown = sorted(dictionary, key=dictionary.get, reverse=True)[:k]
        return most_shown