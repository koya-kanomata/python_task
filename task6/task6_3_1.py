import task6_3_2
import pandas as pd

url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
app_id = "1021298500308407354"

search_keyword = '腕時計'
# 入力パラメーター(公式ホームページを参照)
search_criteria = {
        "format" : "json",
        "keyword" : search_keyword,
        "applicationId" : app_id,
        "availability" : 0,
        "hits" : 30,
        "sort" : "+itemPrice"    
        }

# 出力パラメーター(公式ホームページを参照)
output_parameter = ['itemName', 'itemPrice', 'postageFlag']

#上記記載のクラスを読み出す
rakutenApi = task6_3_2.rakuten_api('https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706')


result = rakutenApi.dataInport(search_criteria, output_parameter)

#pandasでCSV出力
df = pd.DataFrame(result, columns=output_parameter)
df.to_csv('result.csv', index=False)