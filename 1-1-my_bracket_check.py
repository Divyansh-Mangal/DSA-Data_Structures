# balancing bracket problem

def balance_bracket(string):
    stack = []

    for index in range(len(string)):
        if string[index] not in ['(',')','[',']','{','}']:
            pass
        else:
            if string[index] in ['(', '[', '{']:
                stack.append(index)
            elif len(stack) == 0:
                return index + 1
            elif (string[index] == ')' and string[stack[-1]] != '(') or (string[index] == ']' and string[stack[-1]] != '[') or (string[index] == '}' and string[stack[-1]] != '{'):
                return index + 1
            else:
                stack.pop()

    if len(stack) != 0:
        return stack[0] + 1
    else:
        return 'Success'

if __name__ == '__main__':
    string = input()
answer = balance_bracket(string)
print(answer)
