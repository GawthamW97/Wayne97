class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # map the prerequisites to the course 
        preMap = {i : [] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        path = []
        visited,cycle = set(),set()
        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            path.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return path
                