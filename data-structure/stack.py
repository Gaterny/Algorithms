#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 栈是保存线性数据的容器，它的特点是只能在容器的一端进行push和pop数据，即top端(栈顶)
# 栈是后进先出的(Last In First Out) -->LIFO
# 出栈，入栈，栈顶，栈顶
# 栈可以利用顺序表和链表实现


class Stack(object):
    """栈结构"""

    def __init__(self):
        self.__stack = []

    def push(self, item):
        """压栈"""
        return self.__stack.append(item)
        # self.__stack.insert(0, item) 不使用从头部插入元素是因为时间复杂度为O(n)

    def pop(self):
        """出栈"""
        return self.__stack.pop()

    def peek(self):
        """查询栈顶元素"""
        if self.__stack:
            return self.__stack[-1]
        else:
            return None

    def is_empty(self):
        """判断是否为空栈"""
        return self.__stack == []

    def size(self):
        """栈的元素个数"""
        return len(self.__stack)


if __name__ == "__main__":
    s = Stack()
