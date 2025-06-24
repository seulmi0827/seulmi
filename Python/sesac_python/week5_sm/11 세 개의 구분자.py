def solution(myStr):
    result = myStr.replace("a"," ").replace("b"," ").replace("c"," ").split()
    result2 = [map(strip,result)]
    return result2 if result2 else ["EMPTY"]
