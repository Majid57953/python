def firstUniqChar( s: str) -> int:
    print(list(s))
    for j in s:
        count=0
        for i in s:
            if i==j:
                count+=1
                if count>1:
                    break
        if count==1:
            return j


print(firstUniqChar("aabb"))