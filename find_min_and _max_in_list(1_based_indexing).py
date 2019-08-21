n=int(input())
arr_num=list(map(int,input().split()))[0:n]
print(arr_num.index(min(arr_num))+1,arr_num.index(max(arr_num))+1,sep=" ")
