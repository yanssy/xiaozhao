# -*- coding:utf-8 -*-
"""
汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞
着64片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一
次只能移动一个圆盘。

设移动n个盘子的汉诺塔问题需要g(n)次移动操作来完成。由展示移动过程算法可知g(n)应是三部分之和。
(1) 将n个盘上面的n-1个盘子借助C桩从A桩移到B桩上，需g(n-1)次移动；
(2) 然后将A桩上第n个盘子移到C桩上（1次）；
(3) 最后，将B桩上的n-1个盘子借助A桩移到C桩上，需g(n-1)次。
因而有递归关系：
g(n)=2*g(n-1)+1
初始条件(递归出口)：
g(1)=1
即 1、3、7、15、31。。。即g(n) = 2^n -1
"""


def move(n, Source, Temp, Target):
    if n == 1:
        print Source, '->', Target
    else:
        move(n-1, Source, Target, Temp)
        print Source, '->', Target
        move(n-1, Temp, Source, Target)

if __name__ == '__main__':
    move(3, 'Source', 'Temp', 'Target')