from mysql import connector
import stackprinter
"""
mysql数据库的增删改查

1.首先本地启动mysql： docker-compose -f second_step/example/mysql.yml up
2.运行以下命令
python.exe .\second_step\s6.py

参考：https://cloud.tencent.com/developer/article/1151812

"""
class Model:
    def __init__(self):
        db = connector.connect(host="127.0.0.1",user="root",passwd="1234",port=3311,database="fruit")
        self.db =db
        self.cursor = db.cursor()
    
    def insert(self,tableName,fruitDict):
        table = tableName
        keys = ', '.join(fruitDict.keys())
        values = ', '.join(['%s'] * len(fruitDict))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=tableName, keys=keys, values=values)
        try:
            self.db.cursor().execute(sql, tuple(fruitDict.values()))
            self.db.commit()
        except:
            self.db.rollback()
            stackprinter.show(style='plaintext', source_lines=4)
    
    def update(self,tableName,fruitDict,condition):
        table = tableName
        newKeys = [f'{v} = %s' for v in fruitDict.keys()]
        keys = ', '.join(newKeys)
        sql = f'UPDATE {tableName} SET {keys}  WHERE {condition}'
        try:
            self.db.cursor().execute(sql, tuple(fruitDict.values()))
            self.db.commit()
        except:
            self.db.rollback()
            stackprinter.show(style='plaintext', source_lines=4)
    
    def updateOrInsert(self,tableName,fruitDict):
        table = tableName
        keys = ', '.join(fruitDict.keys())
        values = ', '.join(['%s'] * len(fruitDict))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
        update = ','.join([" {key} = %s".format(key=key) for key in fruitDict])
        sql += update
        try:
            self.db.cursor().execute(sql, tuple(fruitDict.values())*2)
            self.db.commit()
        except:
            self.db.rollback()
            stackprinter.show(style='plaintext', source_lines=4)
    
    
    def delete(self,tableName,condition):
        sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=tableName, condition=condition)
        try:
            self.db.cursor().execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            stackprinter.show(style='plaintext', source_lines=4)
    
    def find(self):
        self.cursor.execute("select * from fruit limit 2")
        fruit = self.cursor.fetchall()
        return list(fruit)

if __name__ == "__main__":
    m = Model()
    # m.update("fruit",{
    #     "code":"apple",
    #     "name":"apple",
    #     "color":"yellow"
    # },"id = 1")
    b=m.find()
    print(f"search result:{b}")
    # insert
    m.updateOrInsert("fruit",{
        "code":"pear",
        "name":"pear",
        "color":"blue"
    })
    # update
    m.updateOrInsert("fruit",{
        "id":1,
        "code":"apple",
        "name":"apple",
        "color":"yellow"
    })
    m.delete("fruit","code = 'pear'")
  
    