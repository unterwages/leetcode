def generatePossibleNextMoves(s):
    move=[]
    if len(s)<2:
        return move

    for i in range(len(s)-1):
        if s[i] + s[i+1] == "++":
            move.append(s[:i] + "--" + s[i+2:])
    return move

print generatePossibleNextMoves('++++')
