#coding=utf8
'''
Created on 2017年2月16日

@author: Bigcat
'''


class Foo:
    animal = '兔子'

    def __init__(self, feature):
        self.feature = feature

    # 定义普通方法，至少有一个self参数 """
    def print(self):
        print('调用了普通方法')
        # 同时输出类变量和实例变量
        print('{0}的特征是：{1}'.format(self.animal, self.feature))

    @classmethod
    # 定义类方法，至少有一个cls参数
    def enemy(cls, name):
        print('调用了类方法')
        # enemyName类方法内的变量，类外不可用
        enemyName = name
        # 通过类名.类变量名访问类变量（静态变量）
        print('{0}的天敌是{1}'.format(cls.animal, enemyName))

    @staticmethod
    # 定义静态方法 ，无默认参数
    def eat(name):
        print('调用了静态方法')
        # eatName静态方法内的变量，类外不可用
        eatName = name
        print('{0}的食物是{1}'.format(Foo.animal, eatName))


if __name__ == '__main__':
    # 初始化实例对象
    t = Foo(['长耳朵', '三瓣嘴', '两颗大门牙', '毛柔软', '红眼睛'])
    # 利用实例对象调用普通方法
    t.
    print()
    # 通过实例对象调用类方法
    t.enemy(['狼', '老鼠'])
    # 通过类名调用类方法
    Foo.enemy(['黄鼠狼', '狐狸'])
    # 通过实例对象调用静态方法
    t.eat(['青草', '胡萝卜', '白菜', '薯类'])
    # 通过类名调用静态方法
    Foo.eat(['苹果', '南瓜', '蒲公英', '车前草'])


