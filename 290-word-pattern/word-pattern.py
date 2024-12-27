class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_word = s.split(" ")
        r = {}
        if len(pattern) != len(list_word):
            return False
        flag = 0
        for char in pattern:
            if not char in r:
                r[char] = [list_word[flag]]
            else:
                r[char].append(list_word[flag])
            flag += 1

        r2 = []
        for data in r.values():
            if len(list(set(data))) != 1:
                return False
            r2.append(list(set(data))[0])
        if len(list(set(r.keys()))) != len(list(set(r2))) :
            return False
        return True
