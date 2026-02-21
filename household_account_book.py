# 簡易家計簿
# 文字列は’’でかこう
# 予算
budgets = {'食費': 30000, '娯楽': 15000, '交通費':10000, 'その他':20000}

# 実際の支出
spents = {'食費':0, '娯楽':0, '交通費':0, 'その他':0}

while True:
  input_spent_log = input('いくら使いましたか？半角数字で入力してください：')
  spent_log = int(input_spent_log)
  input_spent_category = input('その支出のカテゴリーは何ですか？食費/娯楽/交通費/その他/追加：')
  if input_spent_category == '追加':
    input_spent_category_add = input('追加したいカテゴリーの名前を入力してください：')
    # 辞書に要素の追加をするときは辞書名[新しいキー名] = 値
    spents['input_spent_category_add'] = spent_log
  else:
    spents[input_spent_category] += spent_log
  input_continueyn = input('これで今月の入力を終了しますか？yes0/no1:')
  continueyn = int(input_continueyn)
  if continueyn == 1:
    continue

for category in spents:
  print(category + 'の合計は' + str(spents[category]) + '円です')
  total_spents += spents[category]
  remains[category]= budgets[category] - spents[category]
print('総支出は' + str(total_spents) + '円です')
for category in remains:
  print('カテゴリー' + category + 'の残金は' + remains[category] + '円です')
  if remains[category] < 0:
    print('予算オーバーです。使いすぎです')
