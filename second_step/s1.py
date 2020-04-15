import json
import dto

"""
1. json字符串，dict，对象，之间的相互转换

python.exe .\second_step\s1.py

"""

fruitDictList = [{
    "name":"apple",
    "price":6.5,
},{
    "name":"pear",
    "price":3.6,
}]

def strAndDict():
    print("dict 和 string之间的转化：")
    print(f"fruitList===>type:{type(fruitDictList)},value:{fruitDictList}")

    fruitStr = json.dumps(fruitDictList)
    print(f"fruitStr===>type:{type(fruitStr)},value:{fruitStr}")

    newFruitDictList = json.loads(fruitStr)
    print(f"newFruitList===>type:{type(newFruitDictList)},value:{newFruitDictList}")


def dictAndObject():
    print("dict 和 对象之间的转化：")
    fruitStr = json.dumps(fruitDictList)
    fruitDtoList = json.loads(fruitStr,object_hook=dto.FruitDto.fromDict)
    fruitDto = fruitDtoList[0]
    print(f"fruitDto[0]===>type:{type(fruitDto)},value:{fruitDto.__dict__},name:{fruitDto.name}")

    newFruitStr = json.dumps(fruitDtoList,default=dto.FruitDto.toDict)
    print(f"newFruitStr===>type:{type(newFruitStr)},value:{newFruitStr}")

if __name__=="__main__":
    strAndDict()
    dictAndObject()

