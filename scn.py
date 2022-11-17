from random import shuffle, choice
import numpy
from datetime import datetime
from time import sleep


# 摇签方法参考 周易入门 杨军，高夏著，2016.04 P41，P48
def pick():  # 抽签函数，正面定义为2，反面为3
    lis = [2, 3]
    shuffle(lis)
    y = [choice(lis), choice(lis), choice(lis)]
    return y


def dy(cha, b):  # 判断动爻函数，输入变量分别是55差值和 卦象奇偶数
    list1 = [6, 7, 18, 19]
    list2 = [5, 8, 17]
    list3 = [4, 9, 16]
    list4 = [3, 10, 15]
    list5 = [2, 11, 14]
    list6 = [1, 12, 13]
    ym = ''
    if cha in list1:
        m = 0
        if b[m] == 0:
            ym = '上六'
        else:
            ym = '上九'
    if cha in list2:
        m = 1
        if b[m] == 0:
            ym = '六五'
        else:
            ym = '九五'
    if cha in list3:
        m = 2
        if b[m] == 0:
            ym = '六四'
        else:
            ym = '九四'
    if cha in list4:
        m = 3
        if b[m] == 0:
            ym = '六三'
        else:
            ym = '九三'
    if cha in list5:
        m = 4
        if b[m] == 0:
            ym = '六二'
        else:
            ym = '九二'
    if cha in list6:
        m = 5
        if b[m] == 0:
            ym = '初六'
        else:
            ym = '初九'
    return ym


def judge(up, dw):  # 判断卦名
    kun = numpy.array([[0], [0], [0]])
    gen = numpy.array([[1], [0], [0]])
    kan = numpy.array([[0], [1], [0]])
    xun = numpy.array([[1], [1], [0]])
    zhen = numpy.array([[0], [0], [1]])
    lih = numpy.array([[1], [0], [1]])
    dui = numpy.array([[0], [1], [1]])
    qian = numpy.array([[1], [1], [1]])
    ut = ''
    dt = ''
    us = ''
    ds = ''
    if (up == kun).all():
        ut = "上坤"
        us = "☷"
    elif (up == gen).all():
        ut = "上艮"
        us = "☶"
    elif (up == kan).all():
        ut = '上坎'
        us = "☵"
    elif (up == xun).all():
        ut = "上巽"
        us = "☴"
    elif (up == zhen).all():
        ut = "上震"
        us = "☳"
    elif (up == lih).all():
        ut = "上离"
        us = "☲"
    elif (up == dui).all():
        ut = "上兑"
        us = "☱"
    elif (up == qian).all():
        ut = "上乾"
        us = "☰"
    else:
        print("what's wrong")
    if (dw == kun).all():
        dt = "下坤"
        ds = "☷"
    elif (dw == gen).all():
        dt = "下艮"
        ds = "☶"
    elif (dw == kan).all():
        dt = '下坎'
        ds = "☵"
    elif (dw == xun).all():
        dt = "下巽"
        ds = "☴"
    elif (dw == zhen).all():
        dt = "下震"
        ds = "☳"
    elif (dw == lih).all():
        dt = "下离"
        ds = "☲"
    elif (dw == dui).all():
        dt = "下兑"
        ds = "☱"
    elif (dw == qian).all():
        dt = "下乾"
        ds = "☰"
    else:
        print("what's wrong")
    name = ut + dt
    return name, us, ds


def main():  # 主函数
    time1 = datetime.now()
    yq = numpy.zeros((6, 3))  # 设定初始摇签数组
    for n in range(5, -1, -1):  # 每行数据进行摇签
        sleep(0.5)  # 每次摇卦延迟时间
        yq[n, :] = pick()
    a = numpy.sum(yq, axis=1, keepdims=True)  # 对每行数据进行求和，根据每行和的奇偶来判断卦象
    b = numpy.zeros([6, 1], dtype=int)
    for i in range(6):  # 判断奇偶数
        if a[i] % 2 == 1:
            b[i] = 1
        else:
            b[i] = 0
    up = b[0:3, :]
    dw = b[3:6, :]
    (name, us, ds) = judge(up, dw)
    cha = 55 - yq.sum()
    gx = name + "\n\n" + us + "\n" + ds
    return '起卦时间\n' + str(time1) + "\n\n" + gx + "\n\n" + "动爻" + "  " + dy(cha, b)
