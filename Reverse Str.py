def reverseStr(s):
    result= []
    if type(s) == str:
        for i in range(len(s)):
            result.append(s[-(i+1)])
        return ''.join(result)

print reverseStr('sdfwe')
