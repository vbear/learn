# coding=utf-8
address = '李明 13567102011 liming@26.com;\
刘东 13667102012 liudong@163.com;\
张晓 13584023115 zhangxiao@163.com;\
陈旭阳 18884026791 chengxuyang@sohu.com;\
欧阳爸爸 15840236688 ouyangbaba@sina.com;'

name = raw_input('请输入要查找的姓名：')
start = address.find(name)

temp = address[start:]

end = temp.find(";") + start
print(address[start:end])
