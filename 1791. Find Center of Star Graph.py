class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        list_text = edges[0] + edges[1]
        for i in list_text:
            if list_text.count(i) == 2:
                return i
            