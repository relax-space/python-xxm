import pymongo
"""
mongo数据库的增删改查

1.首先本地启动mongodb： docker-compose -f second_step/example/mongo.yml up
2.运行以下命令
python.exe .\second_step\s7.py

参考：https://www.runoob.com/python3/python-mongodb.html

"""
class Model:
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = client["fruit"]
        self.table =self.db["fruit"]
        
    
    def add(self,fruitDict):
        self.table.insert_one(fruitDict)
    
    def update(self,d1,d2):
        self.table.update_one(d1,d2)
    
    def delete(self,fruitDict):
        self.table.delete_one(fruitDict)
    
    def find(self,fruitDict):
        fruit = self.table.find(fruitDict)
        return list(fruit)

if __name__ == "__main__":
    m = Model()
    fruitDict= {"name":"apple","price":100}
    m.add(fruitDict)
    b=m.find({"name":"apple"})
    print(b)
    m.update({"name":"apple"},{"$set":{"price":80}})
    m.delete({"name":"apple"})
    