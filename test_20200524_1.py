# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 示例 1:

# 输入: "()"
# 输出: true
# 示例 2:

# 输入: "()[]{}"
# 输出: true
# 示例 3:

# 输入: "(]"
# 输出: false
# 示例 4:

# 输入: "([)]"
# 输出: false
# 示例 5:

# 输入: "{[]}"
# 输出: true


# way1
class Solution:
    def isValid(self, s: str) -> bool:
        left = {'{': 1, '[': 2, '(': 3}
        right = {'}': 1, ']': 2, ')': 3}
        stack = []
        if s != "":
            if len(s) % 2 != 0 or s[0] in right.keys():
                return False
        for i in s:
            if i in left.keys():
                stack.append(i)
            if i in right.keys():
                if left[stack[-1]] == right[i]:
                    stack.pop(-1)
                else:
                    break
        return len(stack) == 0


# way2
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', 'null': 'null'}
        stack = ['null']  #区别,防止栈为空
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in dic.keys():
                stack.append(i)
            elif dic[stack[-1]] == i:
                stack.pop(-1)
            else:
                return False
        return len(stack) == 1