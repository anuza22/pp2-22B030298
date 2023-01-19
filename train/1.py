a = input()
def solution(string):
    out = ''
    for i in range(len(string)-1, -1, -1):
       out+=string[i]
    return out 


print(solution(a))