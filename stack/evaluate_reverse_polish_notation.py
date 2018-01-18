class Solution(object):
    def evalRPN(self, tokens):
        if not tokens: return
        stack = []
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            if i == '-':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 - v1)
            if i == '*':
                stack.append(stack.pop() * stack.pop())
            if i == '/':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 / v1)
            print(stack)
        return stack.pop()


