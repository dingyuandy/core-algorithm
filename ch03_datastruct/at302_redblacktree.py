#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# at302_redblacktree: 红黑树
"""
    Topic: sample
    Desc : 红黑树
        红黑树是满足下面红黑性质的二叉搜索树：
            1，每个结点或者是红色的，或者是黑色的
            2，根结点黑色
            3，每个叶子结点（None）是黑色的
            4，如果一个结点是红色的，则它的两个子结点都是黑色的
            5，对每个结点，从该结点到其所有后代叶结点的简单路径上，均包含相同数目的黑色结点。
    一个有n个内部结点的红黑树的高度最多为2lg(n+1)
"""
__author__ = 'Xiong Neng'