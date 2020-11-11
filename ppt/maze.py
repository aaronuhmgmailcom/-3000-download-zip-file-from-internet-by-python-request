# 迷宫
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

points = [
    lambda x, y: (x - 1, y),  # 上
    lambda x, y: (x + 1, y),  # 下
    lambda x, y: (x, y - 1),  # 左
    lambda x, y: (x, y + 1),  # 右
]


def maze_path(x1, y1, x2, y2):  # 起点，终点
    # 创建栈，记录行进路径
    stack = [(x1, y1)]
    # 标记起点
    maze[x1][y1] = 7
    # stack中有数据即可查找路径
    while len(stack) > 0:  # stack
        # 记录当前节点
        cur_point = stack[-1]
        # 判断是否走到终点
        if cur_point == (x2, y2):
            print("到达终点")
            # 打印行走路径
            for p in stack:
                print(p)
            return True
        # 下一节点：上下左右
        for po in points:
            # 确定下一节点
            next_point = po(cur_point[0], cur_point[1])
            # 判断下一节点
            if maze[next_point[0]][next_point[1]] == 0:
                # 记录节点
                stack.append(next_point)
                # 移动,标记
                maze[next_point[0]][next_point[1]] = 7
                break
        else:
            # 无法移动，回退
            stack.pop()
    else:
        print("无可行路径")
        return False


maze_path(1, 1, 8, 8)
