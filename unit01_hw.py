# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:39:57 2023

@author: MarkWu
"""
#ie.2
'''
n = int(input('請輸次執行次數：'))
for i in range (n):
    semester = input('請輸入課程期數：')
    course = input('請輸入課程名稱：')
    name = input('請輸入姓名：')
    background = input('請輸入您的背景：')
    expectation = input ('請簡述對於本課程的期望：')
    
    #輸出
    print('-----------------')
    print('第%s期 - %s ' %(semester,course))
    print('姓名：', name,',')
    print('學生背景：',background)
    print('---------------結訓證明--------------')
    print('恭喜', name, "修習完課程[",course,"]後，")
    print('結業成果獲得：', expectation,'。')
    print('Well Done')
    print('-----------------')
'''

#ie.3
'''
import random

#程式變數初始化
Max = 100
Min = 0
ans = random.randint(1, 99)
count = 0
while True:
    print('請輸入',Min,'< ? <',Max,'範圍的數字：',end="")
    guess = int(input())
    #如果guess有在Min & Max的範圍內的話
    if guess > Min and guess < Max:
        #原來猜數字的程式
        count += 1
        if guess == ans:
                print('bingo          ')
                break
        elif guess > ans:
                Max = guess
                print('猜太大，您猜了%d次' %(count))
        else:
                Min = guess
                print('猜太小，您猜了%d次' %(count))
    else:
    #否則的話
        print('out of range')
        #列印('out of range')
'''



