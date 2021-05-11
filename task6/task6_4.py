import requests
import pandas as pd

url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
app_id = "1021298500308407354"
item_id = 100283
serch_params={
    "format" : "json",
    "applicationId" : app_id,
    "genreId" : item_id,
    "page" : 1,
}

response = requests.get(url, serch_params)
result = response.json()

#item_key = ['rank','itemName','	itemPrice','smallImageUrls']

#item_list = []

item_all_list = []
for i in result["Items"]:
    item = i["Item"]
    item_list = {}
    item_list["順位"] = item["rank"]
    item_list["商品名"] = item["itemName"]
    item_list["URL"] = item["itemUrl"]
    item_list["価格"] = item["itemPrice"]
    item_all_list.append(item_list)
print(item_all_list)

df = pd.DataFrame(item_all_list)
df.to_csv('result_6_4.csv', index=False)