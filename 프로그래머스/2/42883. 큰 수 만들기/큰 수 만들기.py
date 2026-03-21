def solution(number, k):
    stack = []
    for n in number:
        while k and stack and stack[-1] < n:
            stack.pop()
            k -= 1
            
        stack.append(n)
        
    return ''.join(stack)[:len(stack) - k]

