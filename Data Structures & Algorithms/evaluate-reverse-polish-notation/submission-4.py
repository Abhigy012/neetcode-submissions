class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = ["+" , "-" , "*" , "/"]
        s = ""
        for x in tokens:
            if x in operators:
                num2 , num1 = st[-1] , st[-2]
                st.pop()
                st.pop()
                if s:
                    s = '(' + s + x + str(num2) + ')'
                else:
                    s =  '(' + str(num1) + x + str(num2) + ')'
                result = 0
                if x == "+":
                    result = num1 + num2
                elif x == "-":
                    result = num1 - num2
                elif x == "*":
                    result = num1 * num2
                else:
                    result = int(num1 / num2)
                print(result)
                st.append(result)
            else:
                st.append(int(x))
        print(s)
        return st[0]