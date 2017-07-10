# stack practise


def solution(S):
    # {}, (), []
    dict = {
        "{":"}", 
        "(":")", 
        "[":"]"
    }
    stack = []
    for c in S:
        if c in dict:
            stack.append(dict[c])
        else:
            if len(stack) > 0 and c == stack[-1]:
                stack.pop()
            # {}}} ==> two many closing signs
            else:
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0

print solution("{[()()]}")
print solution("{[(())()]}")
print solution("{([())]}")
