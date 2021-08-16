## 說明:  
使用找尋保鄉內之寶藏，解說For 迴圈法。 
箱子內裡有不同的寶藏，包含珠寶、新臺幣、首飾、美金、黃金、支票，等著被拿出。
    
  
### 命名: 假設朵拉的箱子為D_box，裡面有裝很多東西
    D_box = ["珠寶", "新臺幣", "首飾", "美金", "黃金", "支票", ""]

### t為找尋次數，初始值第一次因為剛開始找所以設為:0
    t = 0
    
### 執行: 要開始找寶藏了喔! 不曉得有什麼，所以統一用treasure命名為要找的寶藏!
    for treasure in D_box:
        # 只要開始找，就會增加一次找的次數
        t += 1
### 因為朵拉只喜歡黃金，所以她只要找黃金，所以如果找的treasure等於黃金，冒險就結束
        if treasure == "黃金":
            print('找第', t, "次,找到黃金！")
            # 代表找到黃金了，尋寶冒險就結束
            break
#### 因為朵拉只喜歡黃金，所以如果找的treasure不是黃金，就顯示不是找到黃金，是該物品名稱
        else:
            print('找第', t, "次,這個櫃子裡不是黃金,是", treasure)


### [ 以下為原本教學程序 ]
    d = ['a', 'b', 'c', 'q', 'e']
    t = 0
    for i in d:
        t += 1
        if i == "q":
            print('第', t, "次,q！")
            break
        else:
            print('第', t, "次,", i)
        
    
### 結果呈現:
![for_adventure](https://user-images.githubusercontent.com/70878758/129534435-0c74fc49-448d-4672-8e64-d8659ca837b9.png)
