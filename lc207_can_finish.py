from typing import List
from queue import Queue

'''
    拓扑序：在一张有向无环图上，按照序列走所有的点，可以保证在一个点被访问时，它前面的点都已经被访问过了。
    
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 初始化入度数组和出边数组
        inDeg = [0] * numCourses
        to = [[] for _ in range(numCourses)]

        # 构建出边数组和入度数组
        for pre in prerequisites:
            ai = pre[0]
            bi = pre[1]
            to[bi].append(ai)  # 出边数组加边模板
            inDeg[ai] += 1

        q = Queue()
        # 拓扑排序第一步：从零入度点出发
        for i in range(numCourses):
            if inDeg[i] == 0:
                q.put(i)

        lessons = []
        # BFS模板
        while not q.empty():
            x = q.get()
            lessons.append(x)
            # 第二步：扩展一个点，周围的点入度减一
            for y in to[x]:
                inDeg[y] -= 1
                # 第三步：入度减为0，表示可以入队了
                if inDeg[y] == 0:
                    q.put(y)

        # 判断是否可以完成所有课程
        return len(lessons) == numCourses