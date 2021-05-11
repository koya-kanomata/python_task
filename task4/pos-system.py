import pandas as pd
import datetime

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

    def add_item_order(self,item_code):
        if(item_code=="確定"):
#            global sum_fee
#            self.sum_fee=0
            self.pay()
            exit()
        else:    
            order_list[item_code] = master_list[item_code]
            if len(order_list[item_code]) == 2:
                order_list[item_code].append(1)
            else:
                order_list[item_code][2]=order_list[item_code][2]+1
             
            print("{}を買い物かごに追加しました。".format(order_list[item_code][0]))

    
    def view_item_list(self):
        global sum_fee
        global sum
        self.sum_fee=0
        self.sum=0
        
        print("[オーダー]")
        for code in order_list:
            print("商品コード{}".format(code))
            print("商品名{}".format(order_list[code][0]))
            print("価格{}".format(order_list[code][1])) 
            print("個数{}".format(order_list[code][2]))
            print("\n")
        print("----------------------------------")
        print(order_list)
        for order in order_list:
            
            self.sum = self.sum + order_list[order][2]
            self.sum_fee = self.sum_fee + order_list[order][1] * order_list[order][2]
        
        print("商品数:",self.sum,"点")
        print("合計支払金額:",self.sum_fee,"円")

        


    #def view_item_list(self):
     #   for code in order_list:
      #      print("商品コード:{}".format(code))
       #     print("[商品名]{}".format(order_list[code][0]))
        #    print("[価格]{}".format(order_list[code][1]))

    def pay(self):
        
        self.pay_fee = int(input("支払金額を入力してください:"))
        self.charge=self.pay_fee-self.sum_fee
        print("{}円のお返しです。".format(self.charge))
        print("ご利用ありがとうございました。")
        
        self.receipt_num = "お買い上げ数:{}点".format(self.sum)
        self.receipt_sum_fee = "合計金額:{}円".format(self.sum_fee)
        self.receipt_pay_fee = "お預かり金額:{}円".format(self.pay_fee)    
        self.receipt_charge = "お返し金額{}円".format(self.charge)

        with open('./receipt_{}.text'.format(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')),mode='a',encoding='utf-8_sig') as f:
            f.write(self.receipt_num)
            f.write("\n")
            f.write(self.receipt_sum_fee)
            f.write("\n")
            f.write(self.receipt_pay_fee)
            f.write("\n")
            f.write(self.receipt_charge)
            
    
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




### メイン処理
def main():
    # マスタ登録
    add_item_master_by_csv()
    #print("マスタ登録完了")
    # オーダー登録
    order=Order(item_master)
    while True:
        code=input('購入する商品コードを入力してください(「確定」と入力でお支払いへ):')
        print("\n")
        order.add_item_order(code)
        
        # オーダー表示
        order.view_item_list()
    


if __name__ == "__main__":
    main()