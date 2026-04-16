def isEven(n):
    if(n & 1) == 0:
        return True
    else:
        return False
    
#find the sum of the first n natural numbers
# def findSum(n):
#     sum = 0
#     i = 1
#     # for i in range(n+1):
#     #     sum += i
#     while i <= n:
#         sum +=i
#         i +=1
#     return sum
# def findSum(n):
#     #base condition
#     if n ==1:
#         return 1
#     return n + findSum(n-1)

def findSum(n):
    #using mathmatical formula to compute
    #sum of first n natural numbers
    return n*(n+1)//2
if __name__ == '__main__':
    n = 3
    print(findSum(n))