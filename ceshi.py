#! /usr/bin/env/python
# —*— coding:utf-8 -*-


# 校验的
with open(r'C:\Users\admin\Desktop\newshuju.txt','r',encoding='utf8') as a:
    HouTai = a.readlines()
# print(HouTai)
# 完整的
with open(r'C:\Users\admin\Desktop\srcshuju.txt','r',encoding='utf8') as b:
    XuQiu = b.readlines()
# print(XuQiu)
XiangTong = []
c = []
for i in XuQiu:
    # for r in b:
    if i in HouTai:
        XiangTong.append(i)
    else:
        c.append(i)
print(len(XiangTong))
# print(XiangTong)
print("缺少：",len(c))
print("缺少:",c)
print("校验的：",len(HouTai))
print("完整的：",len(XuQiu)) 