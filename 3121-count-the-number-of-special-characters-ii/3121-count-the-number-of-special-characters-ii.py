class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s= {}
        for i in range(len(word)):
            if word[i].islower():
                s[word[i]] = i
            if word[i] not in s:
                s[word[i]] = i
        # print(s)

        uni = set()
        c = 0
        for i in word:
            if i.islower():
                uni.add(i)
        # print(uni)
        uni = list(uni)
        for i in uni:
            # print(s[i])
            if i.lower() in s and i.upper() in s:
                if s[i.lower()]<s[i.upper()]:
                    c+=1
        return c