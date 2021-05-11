import csv

f=open("study/task1/charalist.csv","r",encoding="utf-8")
reader=csv.reader(f,delimiter=',')
s = [line for line in reader]
source=s[0]

answer = input('キャラクター名を入力してください')

for i in range(0,len(source)):
    if(answer==source[i]):
        print('存在します')
        break;
    elif(i==len(source)-1):
        print('存在しません')
        source.append(answer)
        print(answer+'を追加しました')
        with open('study/task1/charalist.csv','w',encoding='utf-8') as f:
          writer=csv.writer(f)
          print(source)
          writer.writerow(source)
    else:
        continue;
