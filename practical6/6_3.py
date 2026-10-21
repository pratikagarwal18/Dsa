def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = []

    for char in expression:
        if char.isalnum():
            postfix.append(char)

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())

            if stack:
                stack.pop()   # Remove '('

        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(char)):
                postfix.append(stack.pop())

            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


expression = input("Enter infix expression: ")

result = infix_to_postfix(expression)

print("Postfix expression:", result)