def s1():
    print("1.===================")
    intArray =[]
    for i in range(2000,3201):
        if i % 7 ==0 and i% 5 != 0:
            intArray.append(str(i))
    print(",".join(intArray))

def s2():
    print("2.===================")
    value = input("请输入一个整数：")
    intV = int(value)
    dict ={}
    for i in range(1,intV+1):
        dict[i]=pow(i,2)
    print(dict)

def s3():
    print("3.===================")
    value = input("请输入一个整数序列（34,67,55,33,12,98）：")
    list= value.split(",")
    t = tuple(list)
    print(f"列表{list}")
    print(f"元组{t}")

class StrDto:
    def __init__(self):
        pass
    def getString(self):
        value = input("请输入英文字母：")
        return value
    def printString(self,rawStr):
        up = rawStr.upper()
        print(up)

def s4():
    print("4.===================")
    dto = StrDto()
    value = dto.getString()
    dto.printString(value)

if __name__ == "__main__":
    s1()
    s2()
    s3()
    s4()