import eel
#import desktop
import possystem

#app_name="html"
#end_point="index.html"
#size=(700,600)

@eel.expose
def order_item(item_code,item_num):
    possystem.main(item_code,item_num)

@eel.expose
def master_item():
    possystem.add_item_master_by_csv()

@eel.expose
def payment(payment,result):
    possystem.payment(payment,result)

#@eel.expose
#def send_item_info(info):
#    possystem.item_info(info)

eel.init("html")
eel.start("index.html")