class Solution:
    def __init__(self):
        pass

    def helper(self, vocabulary, sentence):
        if len(sentence) == 0:
            return [], True

        split = 0
        ret = list()
        while split <= len(sentence):
            prefix = sentence[:split]
            suffix = sentence[split:]
            if prefix in vocabulary:
                res, flag = self.helper(vocabulary, suffix)
                if flag:
                    return [prefix] + res, flag
            split += 1

        return [], False

    def solution(self, vocabulary, sentence):
        sentence, valid = self.helper(vocabulary, sentence)
        if valid:
            return sentence

    def better_solution(self, vocabulary, sentence):
        starts = {0:''}
        for i in range(len(sentence)+1):
            new_starts = starts.copy()
            for start, _ in starts.items():
                word = sentence[start:i]
                if word in vocabulary:
                    new_starts[i] = word
            starts = new_starts.copy()

        curr_len = len(sentence)
        ret = []

        if curr_len not in starts:
            return []

        while curr_len > 0:
            word = starts[curr_len]
            curr_len -= len(word)
            ret.append(word)

        return list(reversed(ret))
