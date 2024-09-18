from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            adj_list[pre].append(course)
        
        visited = [0] * numCourses
        
        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            
            for neighbor in adj_list[course]:
                if not dfs(neighbor):
                    return False
            
            visited[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
