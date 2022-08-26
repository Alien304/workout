def reversinglists(yourtext="Napisz tekst, którego kolejność należy odwrócić: "):
    return str(input(yourtext))

text = reversinglists()

def reverseresult():
    result = text.split()
    result.reverse()
    result = " ".join(result)
    print(result)

reverseresult()

