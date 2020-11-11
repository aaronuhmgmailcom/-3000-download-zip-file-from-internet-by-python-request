class Stack:
    # 初始建立一个空栈
    def __init__(self):
        self.stack = []

    # 判断是否为空
    def is_empty(self):
        return self.stack == []

    # 进栈
    def push(self, element):
        self.stack.append(element)

    # 出栈
    def pop(self):
        if self.is_empty():
            return False
        return self.stack.pop()

    # 查看栈顶
    def get_top(self):
        if self.is_empty():
            return False
        return self.stack[-1]

    # 查看栈底
    def get_down(self):
        if self.is_empty():
            return False
        return self.stack[0]


list_bracket_left = ['(', '[', '{']
list_bracket_right = [')', ']', '}']
match = {')': '(', ']': '[', '}': '{'}


# 匹配括号
def bracket_match(br):
    # 创建一个空栈
    s = Stack()
    # 遍历br中元素
    for item in br:
        if item in list_bracket_left:
            s.push(item)
        elif item in list_bracket_right:
            if s.is_empty():
                return False
            elif s.get_top() == match[item]:
                s.pop()
            else:
                return False
    if s.is_empty():
        return True
    else:  # 多个左括号
        return False


if __name__ == '__main__':
    tt = '({[f({}+-[=])(a){h}g]})[h]jkl'
    print(bracket_match(tt))
