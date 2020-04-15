import sys,os,traceback,json
import dto

"""
练习文件的读写
python.exe .\second_step\s2.py

参考：
https://www.w3cschool.cn/pythonlearn/dfmt1pve.html
https://www.runoob.com/python/file-methods.html
"""


class File:
    def __init__(self):
        pass
    
    def read(self):
        path ="second_step/temp_data/base_test.txt"
        with open(path,mode="rt",encoding="utf-8") as fp:
            content = fp.read()
            return content
        return ""
    
    def write(self,content):
        path ="second_step/temp_data/base_test.txt"
        with open(path,mode="wt",encoding="utf-8") as fp:
            fp.write(content)
    
    def readList(self,path,mode="rt",encoding='utf-8',object_hook=None):
        try:
            contents=[]
            with open(path,mode, encoding=encoding) as fp:
                if object_hook ==None:
                    contents = json.load(fp)
                else:
                    contents = json.load(fp,object_hook=object_hook)
            return contents,None
        except Exception as inst:
            return None,traceback.format_exc()

    def writeList(self,list,dirPath,fileName,mode="w",encoding='utf-8',default=None,ensure_ascii=False):
        fileName="%s/%s" % (dirPath,fileName)
        try:
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)
            with open(fileName, mode, encoding=encoding) as fp:
                if default == None:
                    json.dump(list,
                        fp,ensure_ascii=ensure_ascii)
                else:
                    json.dump(list,
                        fp,default=default,ensure_ascii=ensure_ascii)
            return None
        except Exception as inst:
            return traceback.format_exc()
    
    def base(self):
        print("===> 1.基本  的read 和 write")
        self.write('{"name":"hello world"}')
        content = self.read()
        print(f"type:{type(content)},content:{content}")

    def rwJson(self):
        print("===> 2.json  的read 和 write")
        dict1 = {"name":"你好世界"}
        err= self.writeList(dict1,"second_step/temp_data","file_test.json")
        if err != None:
            print(err)
            return
        content,err = self.readList("second_step/temp_data/file_test.json")
        if err != None:
            print(err)
            return
        print(f"type:{type(content)},content:{content}")
    
    def rwDto(self):
        print("===> 3.dto  的read 和 write")
        fruitDto = dto.FruitDto()
        fruitDto.name = "apple"
        fruitDto.price = 6.5
        err= self.writeList(fruitDto,"second_step/temp_data","dto_test.json",default=dto.FruitDto.toDict)
        if err != None:
            print(err)
            return
        content,err = self.readList("second_step/temp_data/dto_test.json",object_hook=dto.FruitDto.fromDict)
        if err != None:
            print(err)
            return
        print(f"type:{type(content)},content:{content.__dict__}")


if __name__ == "__main__":
    f=File()
    f.base()
    f.rwJson()
    f.rwDto()