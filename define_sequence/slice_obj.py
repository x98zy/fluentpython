"""自定义一个可切片对象"""
from collections import abc
import numbers
class Group():
    def __init__(self,company_name,group_name,staffs):
        self.company_name=company_name
        self.group_name=group_name
        self.staffs=staffs

    def __reversed__(self):
        return self.staffs.reverse()

    def __len__(self):
        return len(self.staffs)

    def __getitem__(self, item):
        cls=type(self)
        if isinstance(item,slice):
            return cls(company_name=self.company_name,group_name=self.group_name,staffs=self.staffs[item])
        if isinstance(item,numbers.Integral):
            return cls(company_name=self.company_name,group_name=self.group_name,staffs=[self.staffs[item]])

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

if __name__=="__main__":
    group=Group(company_name="Microsoft",group_name="user",staffs=["Alice","Bob","Jack","Joe"])
    res=group[0:2]
    pass