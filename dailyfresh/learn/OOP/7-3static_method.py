#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Foo:
    animal='兔子'
   # print type(animal)
    def __init__(self,feature):
        self.feature = feature

    def _print(self):
        print('调用了普通方法')
        #print('{0} 的特征是: {1} '.format(self.animal,self.feature))
        print self.animal,str('的特征是'),str(self.feature).decode('unicode-escape')

    @classmethod
    def enemy(cls,name):
        print('调用了类方法:')
        enemyName=name
        #print('{0}的天敌是{1}'.format(cls.animal,enemyName))
        print cls.animal+str(' 的天敌是'),str(enemyName).decode('unicode-escape')

    @staticmethod
    def eat(name):
        print('调用了静态方法')
        eatName=name
       # print('{0}的食物是{1}'.format(Foo.animal,eatName))
        print Foo.animal,str('的食物是'),str(eatName).decode('unicode-escape')


if __name__ == '__main__':
    t = Foo([u'长耳朵',u'三瓣嘴',u'两颗大门牙',u'毛柔软',u'红眼睛'])
    t._print()
    t.enemy([u'狼',u'老鼠'])
    Foo.enemy([u'黄鼠狼',u'狐狸'])
    t.eat([u'青草',u'胡萝卜',u'白菜',u'薯类'])
    Foo.eat([u'苹果',u'南瓜',u'蒲公英', u'车前草'])