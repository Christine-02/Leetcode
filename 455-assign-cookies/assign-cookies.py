class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        # cookieleft = 0
        childptr=0
        cookieptr=0
        n= len(g)
        m = len(s)
        count=0
        
        while(childptr < n and cookieptr < m):
            if s[cookieptr] >= g[childptr]:
                # cookieleft = g[childptr]-s[cookieptr] 
                count= count+1
                cookieptr = cookieptr+1
                childptr = childptr+1
            else:
                # cookieleft = s[cookieptr] + cookieleft
                cookieptr = cookieptr+1
        return count



                    