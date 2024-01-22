def solution(roman : str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    symbols={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result =0
    for i in range(len(roman)):
        value=symbols[roman[i]]
        if i+1<len(roman) and symbols[roman[i+1]]>value:
            result-=value
        else:
            result+=value 
    return result
print(solution("MCMXC"))