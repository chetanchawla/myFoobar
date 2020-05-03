class Solution:
    def __init__(self):
        pass
    def solution(n):
        lambdaList=''
        num=0
        while len(lambdaList)<10005:
            num=num+1
            if num>1:
                for i in range(2, num):
                   if (num % i) == 0:
                       break
                else:
                   lambdaList=lambdaList+str(num)
        return(lambdaList[n:n+5])
print(Solution.solution(3))