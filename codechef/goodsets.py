l = int(input())
ans=[]
while l > 0:
    l -=1
    y = int(input())
    usr_in = [(int(s)) for s in input().split(" ")]
    result_set = sorted(usr_in)
    for x in range(0,y):
        for i in usr_in:
            if i % usr_in[x] == 0 and i!=usr_in[x]:
                result_set.append([i, usr_in[x]])
            else:
                pass
    print(len(result_set)%1000000007)