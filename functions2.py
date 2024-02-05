def isPalindrome(s: str) -> bool:
    # clean=[]
    # for i in list(s):
    #     if i.isalnum():
    #         clean.append(i.lower())
    # print(len(clean))
    # if len(clean)%2!=0:
    #     tm=int((len(clean)-1)/2)
    # else:
    #     tm=int((len(clean))/2)
    # print(tm)
    # if clean[0:tm]==clean[-1:-tm-1:-1] and len(clean)!=1:
    #     print(True)
    # else:
    #     print(False)

    l = [c for c in s.lower() if c.isalnum()]

    return l == l[::-1]

print(isPalindrome("a"))