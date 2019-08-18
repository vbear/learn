#coding=utf8
import os
#文件批量重命名函数

def imgRename():
    ext = input('清楚如要批量命名的文件后最名词:如:.jpg,txt').strip()
    if ext=='':
        return
    myPath=input("请输入图片文件夹所在文件夹:")
    allFiles=os.listdir(myPath)
    ext_list=[]
    list_len=[]
    for ifile in allFiles:
        fullFile=os.path.join(myPath,ifile)
        if os.path.isfile(fullFile) and os.path.splitext(ifile)[1][1:].lower()==ext:
            ext_list.append(ifile)
            list_len.append(len(ifile))
        if len(ext_list)==0:
            print('未发现*.',ext,'文件类型')
            return
        print('找到如下*.',ext,'文件')
        for ifile in ext_list:
            print(ifile)
        print(25*'*')
        choice=input('你确定要对指定文件夹下匹配后缀批量重命名吗？ Y/y  N/n\n')
        if choice!='Y' and choice !='y':
            return
        else:
            fi_num_cnt=1
            input_max_len=max(list_len)
            preFix=input("请输入文件前缀:\n")

