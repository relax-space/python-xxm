class FruitDto:
    def __init__(self):
        self.name =""
        self.price=0.0

    @classmethod
    def toDict(self,obj):
        dict = obj.__dict__
        return dict

    @classmethod
    def fromDict(self,dict):
        obj = FruitDto()
        obj.__dict__.update(dict)
        return obj