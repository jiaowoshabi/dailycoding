class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, word1, word2, text):
        words = text.split(" ")
        res = len(words)
        for idx, val in enumerate(words):
            if word1 == val:
                fast = idx
                while fast < len(words) and words[fast] != word2:
                    fast += 1
                if fast < len(words) and words[fast] == word2:
                    res = min(res, fast-idx-1)
        return res

    def better_solution(self, word1, word2, text):
        words = text.split(" ")
        word1_indices = [i for i, val in enumerate(words) if val == word1]
        word2_indices = [i for i, val in enumerate(words) if val == word2]

        if not word1_indices or not word2_indices:
            return float('inf')

        i=j=0
        min_distance = abs(word2_indices[j] - word1_indices[i])

        while i < len(word1_indices) and j < len(word2_indices):
            curr_dis = word2_indices[j] - word1_indices[i]
            if curr_dis >= 0:
                min_distance = min(min_distance, curr_dis)
            
            if word1_indices[i] < word2_indices[j]:
                i += 1
            else:
                j += 1
                
        return min_distance-1