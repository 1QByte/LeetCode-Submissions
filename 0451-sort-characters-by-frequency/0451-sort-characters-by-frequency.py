class Solution(object):
    def frequencySort(self, s):
        result = ""
        s_freq = {}
        s_dict = {}

        for i in s:
            if i in s_freq:
                s_freq[i] += 1
            else:
                s_freq[i] = 1

        s_dict = sorted(s_freq.items(), key=lambda item: (-item[1], item[0]))

        result = ''.join(key * value for key, value in s_dict)

        return result
        