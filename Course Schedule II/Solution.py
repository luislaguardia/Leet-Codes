from collections import deque, defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            adj_list[pre].append(course)
            in_degree[course] += 1

        zero_in_degree_queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        topological_order = []

        while zero_in_degree_queue:
            course = zero_in_degree_queue.popleft()
            topological_order.append(course)

            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    zero_in_degree_queue.append(neighbor)

        if len(topological_order) == numCourses:
            return topological_order
        else:
            return []
