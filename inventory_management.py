money = 1000
# 辞書は{キー1: 値1, キー2: 値2, …}
prices = {'apple': 100, 'banana': 200, 'orange': 400}
stocks = {'apple': 3, 'banana': 5, 'orange': 2}
for item in prices:
    print('--------------------------------------------------')
    print('財布には' + str(money) + '円入っています')
    print(item + 'は1個' + str(prices[item]) + '円です')
    # 1個も買えない商品は自動でスキップ
    if money < prices[item]:
        print('1個も買えません')
        continue
    print(item + 'は' + str(stocks[item]) + '個あります')
    while True:
        input_count = input('購入する' + item + 'の個数を入力してください：')
        count = int(input_count)
        total_price = prices[item] * count
        if count > stocks[item]:
            print('在庫が足りません。' + item + 'は' + str(stocks[item]) + '個あります')
            continue
        if money < total_price:
            print('お金が足りません')
            print(item + 'を買えませんでした。最大で' + str(money // prices[item]) + '個なら買えます')
            continue
        break
            
    print('購入する' + item + 'の個数は' + input_count + '個です')
    print('支払い金額は' + str(total_price) + '円です')
    print(item + 'を' + input_count + '個買いました')
    money -= total_price
    # if 文を用いて、 money の値が 0 のときの条件を分岐してください
    if money == 0:
        print('財布が空になりました')
        break
    stocks[item] -= count
    print(item + 'は' + str(stocks[item]) + '個あります')
# 変数 money と型変換を用いて、「 残金は◯◯円です 」となるように出力してください
print('残金は' + str(money) + '円です')
