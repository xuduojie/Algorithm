# 栈
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
top_element = stack.pop()
print(top_element)

# 队列
from collections import deque

# 创建一个队列
queue = deque()
# 入队操作
queue.append(1)
queue.append(2)
queue.append(3)
# 出队操作
item = queue.popleft()  # 弹出并返回队列中的第一个元素
print("出队元素:", item)  # 输出: 出队元素: 1
# 打印剩余队列中的元素
print("剩余队列:", queue)  # 输出: 剩余队列: deque([2, 3])


# 双端队列
from collections import deque

# 将元素依次添加到队列的右端
deque_list = deque()
deque_list.append(1)
deque_list.append(2)

# 将元素依次添加到队列的左端
deque_list.appendleft(3)
deque_list.appendleft(4)

# 弹出队列右端的元素
right_element = deque_list.pop()
print(right_element)

# 弹出队列左端的元素
left_element = deque_list.popleft()
print(left_element)

# 优先队列
import heapq

priority_queue = []

# 将元素添加到优先队列中，并按照元组的第一个元素（优先级）进行排序
heapq.heappush(priority_queue, (3, 'task3'))
heapq.heappush(priority_queue, (1, 'task1'))
heapq.heappush(priority_queue, (2, 'task2'))

# 从优先队列中取出具有最高优先级的元素
highest_priority_task = heapq.heappop(priority_queue)
print(highest_priority_task)  # 输出：(1, 'task1')
