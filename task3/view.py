import eel
import desktop
import search

#app_name="html"
#end_point="index.html"
#size=(700,600)

# eel関数の定義(search.pyに定義している鬼滅キャラ検索関数を呼び出す関数)
@eel.expose
def kimetsu_search(word,csv_name):
    search.kimetsu_search(word,csv_name)

# index.htmlをウィンドウで表示
eel.init("html")
eel.start("index.html")


