class Solution(object):
    def pre_process(self, s):
        return "".join(("$#", "#".join(s), "#"))

    # @return a string
    def longestPalindrome(self, s):
        s_new = self.pre_process(s)
        p = [0]
        center = 0
        mx = 0
        for i in range(1, len(s_new)):
            # 情况2，s[i]不在current_longest_p_str中
            if i > mx:
                p.append(0)
            # 情况1，s[i]在current_longest_p_str中
            else:
                p.append(min(mx - i, p[2 * center - i]))
            # 没办法，只能一个一个去匹配了
            # 注意，对于以s[i]为中心的最长回文子串完完整整包括在current_longest_p_str的情况，while循环不会执行，想想为什么
            while (i - p[i] - 1) > 0 and (i + p[i]  + 1) < len(s_new) and s_new[i - p[i] - 1] == s_new[i + p[i] + 1]:
                p[i] += 1
            # 更新current_longest_p_str相关信息
            if p[i] > mx - center:
                center = i
                mx = i + p[i]
        return s_new[center - p[center]: center + p[center] + 1].replace("#", "")