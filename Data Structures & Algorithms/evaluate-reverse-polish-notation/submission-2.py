class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]
        nums = deque()
        for i in range(len(tokens)):
            if tokens[i] not in operands:
                nums.append(int(tokens[i]))
            else:
                num1 = nums.pop()
                num2 = nums.pop()
                if tokens[i] == "+":
                    nums.append(num2 + num1)
                elif tokens[i] == "-":
                    nums.append(num2 - num1)
                elif tokens[i] == "*":
                    nums.append(num1*num2)
                elif tokens[i] == "/":
                    nums.append(int(num2/num1))
        answer = nums.pop()
        return answer 