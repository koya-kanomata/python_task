import requests
import time

class rakuten_api:

    def __init__(self, url):
        self.url = url


    def dataInport(self, search_criteria, output_parameter):
        r = requests.get(self.url, params=search_criteria)
        response = r.json()
        pages = response['pageCount']

 
        pageList = []
        pageListAll = []


        for p in range(1, pages + 1):         
            parameter = {
                'page': p,
            }
            search_criteria.update(parameter)

           
            r = requests.get(self.url, params=search_criteria)

            response = r.json()

            time.sleep(1)
          
            for r in response['Items']:
                item = r['Item']
                for o in output_parameter:
                    pageList.append(item[o])

                pageListAll.append(pageList)
                pageList = []
        
        print(pageListAll[0])
        print(pageListAll[-1])
        

        #return pageListAll