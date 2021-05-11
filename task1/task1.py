import csv

#同ディレクトリの「charalist.csv」を読み込み、全キャラクターを変数「source」に格納
f=open("./charalist.csv","r",encoding="utf-8")
reader=csv.reader(f,delimiter=',')
s = [line for line in reader]
source=s[0]

#キャラクター入力
answer = input('キャラクター名を入力してください')

#入力したキャラクターの存在有無チェック
for i in range(0,len(source)):
    if(answer==source[i]):
        print('存在します')
        break
    elif(i==len(source)-1):         #charlist最後尾のキャラクターとも一致しない場合存在しないと出力
        print('存在しません')
        source.append(answer)
        print(answer+'を追加しました')
        # charalist.csvmの一覧に追加したキャラクターを書き込み
        with open('./charalist.csv','w',encoding='utf-8') as f:
          writer=csv.writer(f)
          print(source)
          writer.writerow(source)
