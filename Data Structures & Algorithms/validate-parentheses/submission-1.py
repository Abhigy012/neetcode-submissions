class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for x in s:
            if x in ['(' , '{' , '[']:
                st.append(x)
            else:
                if x == ')':
                    if len(st) == 0 or st[-1] != '(':
                        return False
                    else:
                        st.pop() 
                if x == '}':
                    if len(st) == 0 or st[-1] != '{':
                        return False
                    else:
                        st.pop() 
                if x == ']':
                    if len(st) == 0 or st[-1] != '[':
                        return False
                    else:
                        st.pop() 
        return len(st) == 0