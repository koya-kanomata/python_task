import csv
import eel

#鬼滅キャラ検索関数。view.pyから呼び出す。(引数1:キャラクター、引数2:結果出力用CSVファイル名)
def kimetsu_search(word,csv_name):

    answer = word
    csv_file=csv_name

    f=open(csv_file,"r",encoding="utf-8")
    reader=csv.reader(f,delimiter=',')
    s = [line for line in reader]
    source=s[0]
 
 # 結果はindex.html記載のview_log_js関数を使いテキストエリアに出力
    for i in range(0,len(source)):
        if(answer==source[i]):
            print('存在します')
            eel.view_log_js(answer+"はいます")
            break
        elif(i==len(source)-1):
            print('存在しません')
            source.append(answer)
            print(answer+'を追加しました')
            eel.view_log_js(answer+"はいません")
            eel.view_log_js(answer+"を追加しました")
            
            with open(csv_file,'w',encoding='utf-8') as f:
                writer=csv.writer(f)
                print(source)
                writer.writerow(source)
        else:
            continue;

    

#kimetsu_search('きょうじゅうろう', './study/task3/charalist.csv')