list1=[0,1,2,2,3,0,4,2]
def pisplay(name:str):
    print(f'Hi {name}')

def lists(n,lst=[]):
    lst.append(n)
    print(lst)

def anagram(str1:str,str2:str):
    string1=list(str1)
    string1.sort()
    string2=list(str2)
    string2.sort()
    print(string1)
    if string1==string2:
        print('its an anagram')
    else:
        print('its not')

def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) :
        for i in range(m ,m+n):
            nums1[i]=nums2[(i-m)]
        return nums1.sort()

def removeElement(nums: list[int], val: int) -> int:
    while val in nums:
         nums.remove(val)
    return nums

def removeDuplicates( nums: list[int]) -> int:
    return list(set(nums))

def majorityElement(nums: list[int]) -> int:
     print(nums.count)
     return max(nums,key=nums.count)

def RomanToInt(s:str):
    roman_numerals={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    total = 0
    i = 0

    while i < len(s):
        current_value = roman_numerals[s[i]]

        if i + 1 < len(s):
            next_value = roman_numerals[s[i + 1]]
            if current_value < next_value:
                total += next_value - current_value
                i += 2
            else:
                total += current_value
                i += 1
        else:
            total += current_value
            i += 1
    return total

def lengthOfLastWord(s: str) -> int:
    arr=s.split()
    return len(arr[-1])

def longestCommonPrefix(strs: list[str]) -> str:
    result=''
    for i in range(len(strs[0])):
        for word in strs:
            print(strs[0][i])
            if i==len(word) or strs[0][i]!=word[i]:
                return result
        result+=word[i]
        #print(result)   
    


def longest_common_prefix(strings):
    if not strings:
        return ""  # Empty input, return an empty string

    # Sort the strings to find the common prefix between the first and last string
    strings.sort()
    first_string, last_string = strings[0], strings[-1]

    # Compare characters until a mismatch is found
    common_prefix = []
    for i in range(min(len(first_string), len(last_string))):
        if first_string[i] == last_string[i]:
            common_prefix.append(first_string[i])
        else:
            break

    return "".join(common_prefix)

# Example usage:
input_strings = ["geeksforgeeks", "geeks", "geek", "geezer"]

longestCommonPrefix(input_strings)
     
        

