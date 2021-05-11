from selenium import webdriver

url = "https://doda.jp/DodaFront/View/JobSearchList.action?sid=TopSearch&usrclk=PC_logout_kyujinSearchArea_searchButton"
driver = webdriver.Chrome("C:\\Users\Kanomata\Desktop\chromedriver.exe")
driver.get(url)

elem_name = driver.find_elements_by_class_name("company")
elem_name2 = driver.find_elements_by_css_selector('span.company.width688:not(span.status.icoSts02):not(span.status.icoSts04)')
print(elem_name2[0].text)
