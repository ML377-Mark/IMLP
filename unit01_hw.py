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


#ie.4

word = input()
print("你用了 %d 個文字述說內心的想法"%(len(word)))


s = '''漢皇重色思傾國，御宇多年求不得。

楊家有女初長成，養在深閏人未識。

天生麗質難自棄，一朝選在君王側。

回眸一笑百媚生，六宮粉黛無顏色。

春寒賜浴華清池，溫泉水滑洗凝脂；

侍兒扶起嬌無力，始是新承恩澤時。

雲鬢花顏金步搖，芙蓉帳暖度春宵；

春宵苦短日高起，從此君王不早朝。

承歡侍宴無閑暇，春從春遊夜專夜。

後宮佳麗三千人，三千寵愛在一身。

金屋妝成嬌侍夜，玉樓宴罷醉和春。

姊妹弟兄皆列士，可憐光彩生門戶。

遂令天下父母心，不重生男重生女。

驪宮高處入青雲，仙樂風飄處處聞。

緩歌慢舞凝絲竹，盡日君王看不足。

漁陽鼙鼓動地來，驚破霓裳羽衣曲。

九重城闕煙塵生，千乘萬騎西南行。

翠華搖搖行復止，西出都門百餘里；

六軍不發無奈何？宛轉蛾眉馬前死。

花鈿委地無人收，翠翹金雀玉搔頭。

君王掩面救不得，回看血淚相和流。

黃埃散漫風蕭索，雲棧縈紆登劍閣。

峨嵋山下少人行，旌旗無光日色薄。

蜀江水碧蜀山青，聖主朝朝暮暮情。

行宮見月傷心色，夜雨聞鈴腸斷聲。

天旋地轉迴龍馭，到此躊躇不能去。

馬嵬坡下泥土中，不見玉顏空死處。

君臣相顧盡霑衣，東望都門信馬歸。

歸來池苑皆依舊，太液芙蓉未央柳；

芙蓉如面柳如眉，對此如何不淚垂？

春風桃李花開日，秋雨梧桐葉落時。

西宮南內多秋草，落葉滿階紅不掃。

梨園子弟白髮新，椒房阿監青娥老。

夕殿螢飛思悄然，孤燈挑盡未成眠。

遲遲鐘鼓初長夜，耿耿星河欲曙天。

鴛鴦瓦冷霜華重，翡翠衾寒誰與共？

悠悠生死別經年，魂魄不曾來入夢。

臨邛道士鴻都客，能以精誠致魂魄；

為感君王輾轉思，遂教方士殷勤覓。

排空馭氣奔如電，升天入地求之遍；

上窮碧落下黃泉，兩處茫茫皆不見。

忽聞海上有仙山，山在虛無縹緲間。

樓閣玲瓏五雲起，其中綽約多仙子。

中有一人字太真，雪膚花貌參差是。

金闕西廂叩玉扃，轉教小玉報雙成。

聞道漢家天子使，九華帳裡夢魂驚；

攬衣推枕起徘徊，珠箔銀屏迤邐開。

雲鬢半偏新睡覺，花冠不整下堂來。

風吹仙袂飄飄舉，猶似霓裳羽衣舞。

玉容寂寞淚闌干，梨花一枝春帶雨。

含情凝睇謝君王，一別音容兩渺茫。

昭陽殿裡恩愛絕，蓬萊宮中日月長。

回頭下望人寰處，不見長安見塵霧。

唯將舊物表深情，鈿合金釵寄將去。

釵留一股合一扇，釵擘黃金合分鈿。

但教心似金鈿堅，天上人間會相見。

臨別殷勤重寄詞，詞中有誓兩心知，

七月七日長生殿，夜半無人私語時：「

在天願作比翼鳥，在地願為連理枝。」

天長地久有時盡，此恨綿綿無絕期。
'''

print ("------------------------------------------")
#請使用者輸入一文字
#計算該文字在文章出現次數
#列印出現次數

print ("------------------------------------------")
#把文字中 '。，\n；：？「」'的標點符號去除

#目前已知出現最多次的字的次數
#目前已知出現最多次的字
 
print('文章總字數:',len(s))

for astr in s:
    #print(astr)
    act=s.count(astr)
    # 如果 現在這個字出現的次數(act) 大於 目前已知出現最多次字的次數
        #就讓 現在這個字出現的次數 成為 目前已知出現最多次的字的次數
        #還要記錄 現在這個字(astr) 到 目前已知出現最多次的字
else:
    print(maxchar)