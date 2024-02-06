strs=['bat','tab','eat','tba','cat','act']

def anagram_key(string):
    key=''
    for ch in sorted(string):
        key+=ch
    return key

anag_dict={}
for word in strs:
    key=anagram_key(word)
    if key not in anag_dict:
        anag_dict[key]=[]
    anag_dict[key].append(word)
print(list(anag_dict.values()))