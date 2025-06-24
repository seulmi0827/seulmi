def solution(numLog):
    wasd = {1:'w',-1:'s',10:'d',-10:'a'}
    result = ''
    for i in range(len(numLog)-1): #0부터 11
        result += wasd[numLog[i+1]-numLog[i]]
    return result
