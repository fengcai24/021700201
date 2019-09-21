#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import cpca
import json

def split_name(s:str):#将名字从字符串中提取出来
    match = s.split(",")
    return match

def split_num(s:str):#将电话号码从字符串提取出来
    phone = re.search(r'1\d{10}',s).group(0)
    match = re.split(r'1\d{10}',s)
    addr = match[0]+match[1]#将电话号码提取出来后，连接两个被分开的字符串
    return (phone, addr)

def solve_5(str0:str):
    #str0 = input()
    #print(str0)
    if str0[-1] == ".":
        str0=str0.split(".")[0]
    s1 = split_name(str0)
    name = s1[0]
    s2 = split_num(s1[1])
    phone = s2[0]
    addr0 = s2[1]
    #print(name, phone, addr0, end="\n")
    df = cpca.transform([addr0])#必须使用列表才能映射
    #print(df)
    #print(dict(df.iloc[0,0:4]))
    tmp = dict(df.iloc[0,0:4])
    addr1 = tmp['地址']#提取出详细地址
    #镇,乡
    zhen = xiang = jiedao = lu = xiang1 = None#init
    if "镇" in addr1:
        zhen = addr1.split("镇")[0]+"镇"
        addr1 = addr1.split("镇")[1]
    if "乡" in addr1:
        xiang = addr1.split("乡")[0]+"乡"
        addr1 = addr1.split("乡")[1]
    if "街" in addr1:
        if "街道" in addr1:
            jiedao = addr1.split("街道")[0] + "街道"
            addr1 = addr1.split("街道")[1]
        else:
            jiedao = addr1.split("街")[0]+"街"
            addr1 = addr1.split("街")[1]
    if "路" in addr1:
        lu = addr1.split("路")[0]+"路"
        addr1 = addr1.split("路")[1]
    if "巷" in addr1:
        xiang1 = addr1.split("巷")[0]+"巷"
        addr1 = addr1.split("巷")[1]


    addr = [tmp['省'],tmp['市'],tmp['区'],"","",]
    if zhen != None:
        addr[3] += (zhen)
    if xiang != None:
        addr[3] += (xiang)


    if jiedao != None:
        addr[3] += (jiedao)
    if lu != None:
        addr[4] += (lu)
    if xiang1 != None:
        addr[4] += (xiang1)
    if jiedao==None:
        if lu==None:
            if xiang1==None:
                if zhen == None:
                    if xiang == None:
                        addr[4] = ""


    addr[4] +=  addr1

    info = {
        "姓名": name,
        "手机": phone,
        "地址": addr
    }
    #编码成json类型数据
    info_data = json.dumps(info, ensure_ascii=False)
    print(info_data)
    #print(json.loads(info_data))#打印结果

def solve_7(str0:str):
    #str0 = input()
    #print(str0)
    if str0[-1] == ".":
        str0=str0.split(".")[0]
    s1 = split_name(str0)
    name = s1[0]
    s2 = split_num(s1[1])
    phone = s2[0]
    addr0 = s2[1]
    #print(name, phone, addr0, end="\n")
    df = cpca.transform([addr0])#必须使用列表才能映射
    #print(df)
    #print(dict(df.iloc[0,0:4]))
    tmp = dict(df.iloc[0,0:4])
    addr1 = tmp['地址']#提取出详细地址
    #镇,乡
    zhen = xiang = jiedao = lu = xiang1 = None#init
    if "镇" in addr1:
        zhen = addr1.split("镇")[0]+"镇"
        addr1 = addr1.split("镇")[1]
    if "乡" in addr1:
        xiang = addr1.split("乡")[0]+"乡"
        addr1 = addr1.split("乡")[1]

    #路,巷,街道
    if "街" in addr1:
        if "街道" in addr1:
            jiedao = addr1.split("街道")[0] + "街道"
            addr1 = addr1.split("街道")[1]
        else:
            jiedao = addr1.split("街")[0]+"街"
            addr1 = addr1.split("街")[1]
    if "路" in addr1:
        lu = addr1.split("路")[0]+"路"
        addr1 = addr1.split("路")[1]
    if "巷" in addr1:
        xiang1 = addr1.split("巷")[0]+"巷"
        addr1 = addr1.split("巷")[1]

    if re.search(r"\d*号",addr1) is None:
        hao = None
    else:
        hao = re.search(r"\d*号",addr1).group(0)
        addr1 = addr1.split("号")[1]


    addr = [tmp['省'],tmp['市'],tmp['区'],"","","",]
    if zhen != None:
        addr[3] += zhen
    if xiang != None:
        addr[3] += xiang
    #print(addr)
    if jiedao != None:
        if zhen is None and xiang is None:
            addr[3] += jiedao
        else:
            addr[4] += jiedao
    if lu != None:
        addr[4] +=lu
    if xiang1 != None:
        addr[4] += xiang1
    if hao != None:
        addr[5] += hao


    addr.append(addr1)

    info = {
        "姓名": name,
        "手机": phone,
        "地址": addr
    }
    #编码成json类型数据
    info_data = json.dumps(info, ensure_ascii=False)
    print(info_data)
    #print(json.loads(info_data))#打印结果


str0 = input()
level = str0.split("!")[0]
level = int(level)
str0 = str0.split("!")[1]
if level == 1:
    solve_5(str0)
if level == 2:
    solve_7(str0)
if level == 3:
    solve_7(str0)
