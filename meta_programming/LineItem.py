"""实现可读可写的特性"""

class LineItem1():
    def __init__(self,weight,price):
        self.weight=weight
        self.price=price
    def total(self):
        return self.weight*self.price

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self,value):
        if value>0:
            self._weight=value
        else:
            raise ValueError("weight值必须大于0")


class LineItem():
    """改进版LineItem"""
    def __init__(self,weight,price):
        self.weight=weight
        self.price=price

    def get_weight(self):
        return self._weight

    def set_weight(self,value):
        if value>0:
            self._weight=value
        else:
            raise  ValueError("weight must be positive")

    weight=property(fget=get_weight,fset=set_weight)


if __name__=="__main__":
    item=LineItem(-2,5)
    print(item.weight)