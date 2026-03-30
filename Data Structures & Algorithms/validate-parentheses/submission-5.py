from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        counter=0
        if len(s)==1:
            return False
        for char in s:
            if char in "{[(":
                stack.append(char)
                counter+=1
            else:
                if len(stack)!=0:
                    removed = stack.pop()
                    if char == ")" and removed in "{[" or char == "}" and removed in "[(" or char == "]" and removed in "{("  :
                        return False
                else:
                    return False
        if counter == len(stack) or len(stack)!=0:
            return False
        
        return True

            