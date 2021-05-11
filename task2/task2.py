import os
from selenium import webdriver
from selenium.webdriver import Chrome,ChromeOptions
import time
import pandas as pd
import csv

#変数宣言(ログファイル、csvファイル)
LOG_FILE_PATH = './log_file.log'
CSV_FILE = "./task2_csv.csv"



#ログ出力関数
def log(txt):
    with open(LOG_FILE_PATH,'a',encoding="utf-8-sig") as f:
        f.write(txt)
    
#メイン処理

# クローム起動    
def main():
    log("処理開始")
    search_keyword=input("キーワードを入力してください:")
    log("キーワード:"+search_keyword+"で検索")
    driver = webdriver.Chrome("C:\\Users\Kanomata\Desktop\chromedriver.exe")
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(5)

    #ポップアップを閉じる
    try:
        driver.execute_script('document.querySelector(".karte-close").click()')
        time.sleep(5)
        driver.execute_script('document.querySelector(".karte-close").click()')
    except:
        pass

    
# キーワード検索
    search_form = driver.find_element_by_class_name("topSearch__text")
    search_form.send_keys(search_keyword)
    search_btn=driver.find_element_by_class_name("topSearch__button")
    search_btn.click()

# 変数宣言
    company_name_null_list = []
    sell_point_null_list = []
    employee_status_null_list = []
    pay_null_list = []
    i=1
    count=1
    success=1
    fail=1

    while True:
    #検索ワードでヒットした募集の会社名、セールスポイント、就業ステータス、給料を抽出
        company_name_list = driver.find_elements_by_css_selector(".cassetteRecruit__heading .cassetteRecruit__name")
        sell_point_list = driver.find_elements_by_css_selector(".cassetteRecruit__heading .cassetteRecruit__copy")
        employee_status_list = driver.find_elements_by_css_selector(".cassetteRecruit__heading .labelEmploymentStatus")
        pay_list = driver.find_elements_by_css_selector(".cassetteRecruit .tableCondition")
    
        for company_name, sell_point, employee_status, pay in zip(company_name_list,sell_point_list,employee_status_list,pay_list):        
            try:
                company_name_null_list.append(company_name.text)
                sell_point_null_list.append(sell_point.text)
                employee_status_null_list.append(employee_status.text)
                pay_null_list.append(pay.text)
                log("抽出成功("+str(success)+"/"+str(count)+"回目)")
                print("抽出成功("+str(success)+"/"+str(count)+"回目)")
                success=success+1
                
            except Exception as e:
                log("抽出失敗("+str(fail)+"/"+str(count)+"回目)")
                log(e)
                print("抽出失敗("+str(fail)+"/"+str(count)+"回目)")
                fail=fail+1
            finally:
                count=count+1     
        
        search_next = driver.find_elements_by_class_name("iconFont--arrowLeft")

        #「次のページ」ボタンが一ページに二つあれば次のページへ、なければ終了
        if len(search_next) == 2:
            next_page_link = search_next[0].get_attribute("href")
            driver.get(next_page_link)
            print(i,"ページ目終了")
            i=i+1
            time.sleep(5)
        else:
            print("全ページ終了")
            log("抽出処理終了")
            break

#csv出力
    df = pd.DataFrame({
        "企業名":company_name_null_list,
        "セールスポイント":sell_point_null_list,
        "採用ステータス":employee_status_null_list,
        "初年度年収":pay_null_list,
        })
        
    df.to_csv(CSV_FILE,encoding="utf-8-sig")

# main処理実行    
if __name__ == "__main__":
    main()