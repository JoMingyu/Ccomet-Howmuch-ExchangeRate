import requests
import json


class Parser:
    def __init__(self):
        country_codes = "AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAM,USD,BDT,BGN,BHD,BIF,SGD,BOV,BRL,BSD,INR,BWP,BYR,BZD,CAD,CDF,CHW,CHF,CLP,CNY,COU,CRC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,EUR,FJD,FKP,GBP,GEL,GHS,GIP,GMD,GNF,GTQ,GYD,HKD,MOP,HNL,HRK,HUF,IDR,ILS,NPR,IQD,IRR,ISK,JMD,JOD,JPY,KES,KGS,THB,KMF,KPW,KRW,KWD,KYD,KZT,LBP,LKR,LRD,LSL,LYD,MAD,MDL,MGA,MKD,MNT,MRO,MUR,MVR,MWK,MXV,MYR,MZN,NAD,NGN,NIO,NOK,NZD,MOR,PEN,PGK,PHP,PKR,PLN,PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SHP,SLL,SOS,SRD,SSP,STD,SYP,SZL,TJS,TMT,TND,TOD,TRY,TTD,TWD,TZS,UAH,UGX,USN,ZWL,UYU,UZS,VEF,VND,VUV,WST,XAF,XCD,XOF,XPF,YER,ZAR,ZMW" #country_code by string
        list = country_codes.split(",")

        self.code_string = country_codes
        self.code_list = list
        self.APIUrl = "https://api.manana.kr/exchange/rate/"

    def get_currency(self, src):
        response = requests.get(self.APIUrl + src + "/" + self.code_string + ".json")
        return response.content

    @staticmethod
    def process_data(jsonData):
        json_dict = json.loads(jsonData)

        tupleList = []

        for dictData in json_dict:
            string = dictData['name']
            dct = string[:3]
            src = string[3:6]

            rate = round(dictData['rate'], 3)

            if src == dct:
                continue

            data = (src, dct, rate)
            tupleList.append(data)

        return tupleList

if __name__ == '__main__':
    p = Parser()

    for code in p.code_list:
        currencyData = p.get_currency(code)
        currencyList = p.process_data(currencyData)

        for currencyInfo in currencyList:
            print(currencyInfo)