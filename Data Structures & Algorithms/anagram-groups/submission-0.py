class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        groups = []

        for words in range(len(strs)):
            sorted_word = "".join(sorted(strs[words]))

            if sorted_word in mapping:
                mapping[sorted_word].append(strs[words])
            else:
                mapping[sorted_word] = [strs[words]]
        
        for keys, values in mapping.items():
            groups.append(values)
        return groups
        