import pandas as pd
import datetime
import eel

global item_num

master_list={}
order_list={}
#sum=0
#sum_fee=0
### 商品マスタクラス
class Item(object):
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
        
        master_list[self.item_code] = [self.item_name,self.price]
        

    def __str__(self):
        return self.item_code

    def get_price(self):
        return self.price

### オーダークラス
class Order(object):
    
    
    #global sum_fee
    #global sum
    #sum=0
    #sum_fee=0
    def __init__(self,item_master):
        self.item_master=item_master

    
    def add_item_order(self,item_code,item_num):
        global order_list

        self.item_code=item_code        
        self.item_num = int(item_num)


        if(item_code=="確定"):
#            global sum_fee
#            self.sum_fee=0
            self.pay()
            exit()
        else:    
            order_list[self.item_code] = master_list[self.item_code]
            
            #print(len(order_list[item_code]))
            if len(order_list[self.item_code]) == 2:
                order_list[self.item_code].append(self.item_num)
                #print(len(order_list[item_code]))
            else:
                order_list[self.item_code][2]=int(order_list[self.item_code][2])+self.item_num
            print("kkkkkkkkkkkkkkkkkkkkkk")
            print(order_list[self.item_code][0])
            print("{}を",self.item_num,"つ買い物かごに追加しました。".format(order_list[self.item_code][0]))
    
    def view_item_list(self):
        print("aaaaaaaaaaaaaaaaaaaa")
        print(self.item_num)

        global sum_fee
        global sum
        self.sum_fee=0
        self.sum=0
        
        eel.view_clear_js()
        print("[オーダー]")
        print(order_list)
        for code in order_list:
            print("商品コード{}".format(code))
            #eel.view_log_js("商品コード{}".format(code))
            print("商品名{}".format(order_list[code][0]))
            #eel.view_log_js("商品名{}".format(order_list[code][0]))
            print("価格{}".format(order_list[code][1])) 
            #eel.view_log_js("価格{}".format(order_list[code][1]))
            print("個数{}".format(order_list[code][2]))
            print("\n")
         
        print("----------------------------------")
        for order in order_list:
            
            self.sum = self.sum + int(order_list[order][2])
            self.sum_fee = self.sum_fee + order_list[order][1] * order_list[order][2]
            print(order_list)
            eel.view_log_js("商品コード{}\n".format(order)+"商品名{}\n".format(order_list[order][0])+"価格{}\n".format(order_list[order][1])+"個数{}\n".format(order_list[order][2]))
        eel.view_log_js("----------------\n"+"商品数:{}\n".format(self.sum)+"合計支払金額:{}\n".format(self.sum_fee))
        
    
        

        print("商品数:",self.sum)
        print("合計支払金額:",self.sum_fee)
        
            
        


    #def view_item_list(self):
     #   for code in order_list:
      #      print("商品コード:{}".format(code))
       #     print("[商品名]{}".format(order_list[code][0]))
        #    print("[価格]{}".format(order_list[code][1]))

def payment(payment,result):   
    sp_info = result.split()
    #print("nnnnnnnnnnnnnnnnn")
    #print(sp_info)
    n=0
    for line in sp_info:
        if line == "----------------":
            sp_info2 = sp_info[n+1]
            print("eeeeeeeeeee")
            print(sp_info[n+1])
            sp_info_sum = int(sp_info2[4:])
            sp_info3 = sp_info[n+2]
            sp_info_sum_fee = int(sp_info3[7:])
        n=n+1

    #sp_info3 = sp_info[6]
   #sp_info_sum_fee = int(sp_info3[7:])
 
    payment = int(payment)

    #payment=int(payment)    
    #self.pay_fee = int(input("支払金額を入力してください:"))
    charge=payment-sp_info_sum_fee
    print("{}円のお返しです。".format(charge))
    eel.receipt_view_js("{}円のお返しです。\nご利用ありがとうございました。".format(charge))
        
    receipt_num = "お買い上げ数:{}点".format(sp_info_sum)
    receipt_sum_fee = "合計金額:{}円".format(sp_info_sum_fee)
    receipt_pay_fee = "お預かり金額:{}円".format(payment)    
    receipt_charge = "お返し金額{}円".format(charge)

    with open('./receipt_{}.text'.format(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')),mode='a',encoding='utf-8_sig') as f:
        f.write(receipt_num)
        f.write("\n")
        f.write(receipt_sum_fee)
        f.write("\n")
        f.write(receipt_pay_fee)
        f.write("\n")
        f.write(receipt_charge)
    exit()

    
    def receipt(self):
        self.view_item_list()
        print("お預かり金額:",self.pay_fee)
        print("お返し:",self.charge)
        return        
    

def add_item_master_by_csv():
    global item_master
    item_master=[]
    #try:
    item_master_df=pd.read_csv('./master.csv',dtype={"item_code":object}) 
    for item_code,item_name,price in zip(list(item_master_df["item_code"]),list(item_master_df["item_name"]),list(item_master_df["price"])):
        item_master.append(Item(item_code,item_name,price))
        #print("{},{}({})".format(item_code,item_name,item_code))
        #return item_master
    #except:
    #    print("マスタ登録が失敗しました")
    #    print("------- マスタ登録完了 ---------")
    #order=Order(item_master)
    
def item_info(info):
    
    sp_info = info.split()
    sp_info2 = sp_info[5]
    sp_info_sum = sp_info2[4:]
    
    sp_info3 = sp_info[6]
    sp_info_sum_fee = sp_info3[7:]

    print(sp_info_sum)
    print(sp_info_sum_fee)    


### メイン処理
def main(item_code,item_num):
    # マスタ登録
    #add_item_master_by_csv()
    #print("マスタ登録完了")
    # オーダー登録
    order=Order(item_master)
    #while True:
    order.add_item_order(item_code,item_num)
        
        # オーダー表示
    order.view_item_list()
    


if __name__ == "__main__":
    main()