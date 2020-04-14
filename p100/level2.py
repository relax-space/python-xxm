import math,re

def s6():
    value = "100,150,180"
    intList = value.split(",")
    resultList = []
    for v in intList:
        new = int((2* 50 * int(v))/30)
        resultList.append(str(int(math.sqrt(new))))
    print(",".join(resultList))


def s7():
    rawList = ["没有","你好","袋","世界"]
    rawList.sort(reverse=True)
    print(rawList)

def s8():
    rawList = ["without","hello","bag","world"]
    rawList.sort()
    print(rawList)

def s9():
    rawStr ="Hello world world Practice makes perfect"
    strDict = {v.upper():"" for v in rawStr.split(" ")}
    print(" ".join(strDict.keys()))

def s10():
    rawStr="hello world! 123"
    str = "".join(re.findall(r"[a-zA-Z]",rawStr))
    numb = "".join(re.findall(r"[0-9]",rawStr))
    print(f"字母{len(str)}数字{len(numb)}")

def s11():
    s = 9
    print(s * 4 + s * 10 * 3 + s* 100*2 + s*1000)


if __name__ == "__main__":
    s6()
    s7()
    s8()
    s9()
    s10()
    s11()