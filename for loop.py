D_box = ["珠寶", "新臺幣", "首飾", "美金", "黃金", "支票", ""]
t = 0
for treasure in D_box:
    t += 1
    if treasure == "黃金":
        print('找第', t, "次,找到黃金！")
        break
    else:
        print('找第', t, "次,這個櫃子裡不是黃金,是", treasure)

        
# [ 以下為原本教學程序 ]
d = ['a', 'b', 'c', 'q', 'e']
t = 0
for i in d:
    t += 1
    if i == "q":
        print('第', t, "次,q！")
        break
    else:
        print('第', t, "次,", i)
