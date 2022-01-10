#第一題
def calculate(min, max):
    sum=0
    for n in range(min,max+1):
        sum=sum+n
    print(sum)

calculate(1, 3)
calculate(4, 8) 



#第二題
def avg(data):
    number=data["count"]  #取得data字典裡count的value，可得員工數量:3
    
    total=0         
    x=0
    list=data["employees"]   #從data字典裡employees的value，取得員工資料的[列表]
    for x in range(number):
        s=list[x]["salary"]     ##s要放在迴圈裡  #從員工資料的列表中，取第x項字典裡salary的value
        total+=s
    
    result=total/number 
    print(result)   

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式

#第三題
from typing import Counter


def maxProduct(nums):
    count=len(nums)               #O(t)
    A=list()            #O(t)
    for n1 in range(count-1):            #O(n)
        for n2 in range(1,count):            #O(n)
            v1=nums[n1]
            v2=nums[n2]
            if v1==v2:
                continue
            elif n2<n1:
                continue
            else:
                result=v1*v2
                A.append(result)
                #print(result)   #最後可刪
    
    M=max(A)              #O(t)
    print(M)              #O(t)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

#第四題                #思考:如果要出現兩組以上的答案?
def twoSum(nums, target):
    count=len(nums)
    A=list()
    for x in range(count):
        for y in range(1,count):
            if x==y:
                continue
            elif nums[x]+nums[y]==target:
                A.append(x)
                A.append(y)
                return A
            else:
                continue

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
#print(type(result))

#第五題 #暫時放棄 
# def maxZeros(nums):
#     n=0
#     A=list()
#     for x in range(len(nums)-1):
#         if nums[x]==nums[x+1]==0:
#             n+=1
        
#         elif nums[x]<nums[x+1]:
#             n+=1
#             A.append(n)
#             print(A)
#             break
#             #if nums[n+2]=="":
#             #     n+=1
#             #     A.append(n)
#             #     return A
                
#             # elif nums[n+2]==1:
#             #     n+=1
#             #     A.append(n)
#             #     return A 
                
#         else:continue
    
#     A.append(n) 
#     print()    
#     M=max(A)
#     print(M)
# # 請用你的程式補完這個函式的區塊
# maxZeros([0, 1, 0, 0]) # 得到 2
# maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
# maxZeros([1, 1, 1, 1, 1]) # 得到 0
# maxZeros([0, 0, 0, 1, 1]) # 得到 3


# #用二分法取代for迴圈,使時間複雜度從O(n)變成O(log n)

# def binary(numbers,find):
#     low=0
#     high=len(numbers)-1
#     n=1    #n=1不可以放在while裡，不然每次加上去的n就會被重置為1
#     while low<=high:
#         mid=low+((high-low)//2)  #// 代表取整數
#         if numbers[mid]<find:
#             low=mid
#             n+=1
#         elif numbers[mid]>find:
#             high=mid
#             n+=1
#         else:
#             break
#     print(mid)
#     print(numbers[mid])
#     print ("第",n,"次找到",find)
# #題目來源:https://reurl.cc/oedNZq

# binary([5,17,33,41,55,61,80],55)
# #binary([2,4,6,8,10,12,14],14)
# #以上方法為錯誤的~ 因為這樣會永遠找不到2和14

# def binary(numbers,find):
#     low=0
#     high=len(numbers)-1
#     n=1    
#     while low<=high:
#         mid=low+((high-low)//2) 
#         if numbers[mid]<find:
#             low=mid+1    #mid要+-1是因為如果mid是答案的話就會直接跳出去了，所以不用再考慮他
#             n+=1
#         elif numbers[mid]>find:
#             high=mid-1    #把中間的數-1以靠近我們要找的值
#             n+=1
#         else:
#             break
#     print(mid)
#     print(numbers[mid])
#     print ("第",n,"次找到",find)   

# binary([2,4,6,8,10,12,14],14)
# binary([1,2,3,4,5,6],1)
# binary([1,2,3,4,5,6],2)
