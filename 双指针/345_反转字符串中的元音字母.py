class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'ioeauIOEAU'
        n = len(s)
        s1 = list(s)
        i, j = 0, n - 1
        while i < j:
            while i < n and not s1[i] in vowels:
                i += 1
            while j > 0 and not s1[j] in vowels:
                j -= 1
            if i < j:
                s1[i], s1[j] = s1[j], s1[i]
                i += 1
                j -= 1
        return ''.join(s1)


if __name__ == '__main__':
    print(Solution().reverseVowels('hello'))
