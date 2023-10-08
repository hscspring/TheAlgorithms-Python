"""
题目：输入一个递增排序的数组和一个值k，请问如何在数组中找出两个和为k的数字并返回它们的下标？假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。例如，输入数组[1，2，4，6，10]，k的值为8，数组中的数字2与6的和为8，它们的下标分别为1与3。
"""


inp = [1, 2, 4, 6, 8, 10]
k = 8


def run(inp, k):
    p1 = 0
    p2 = len(inp) - 1

    while p1 < p2:
        x = inp[p1] + inp[p2]
        if x == k:
            print(p1, p2)
            p1 += 1
            p2 -= 1
        elif x > k:
            p2 -= 1
        else:
            p1 += 1


run(inp, k)