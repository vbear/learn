#coding=utf8

class Fruit:
    '''this is test fruit.....'''
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __del__(self):
        pass

    def __call__(self,*args,**kargs):
        print('Fruit {0} is tasteful'.format(self.name))

    def __str__(self):
        return 'The price of '+self.name + ' is ' + str(self.price)

    def __getattribute__(self,name):  #获取属性的方法
       return object.__getattribute__(self,name)

    def __setattr__(self,name,value):   #设置属性的方法
        self.__dict__[name] = value

if __name__ == '__main__':
    print('Fruit.__doc__:{0}'.format(Fruit.__doc__))
    obj = Fruit('apple',5.5)
    print('obj.__module__:{0}'.format(obj.__module__))
    print('obj.__class__'.format(obj.__class__)) #输出类
    print('obj.__dict__'.format(obj.__dict__))
    obj()
    print(obj)
    obj.__dict__["_Fruit_price"] = 6.5
    print(obj.__dict__.get("_Fruit_price"))