import requests

import query_formats
from database import Database


class Parser:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        country_codes_all = "AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAM,USD,BDT,BGN,BHD,BIF,SGD,BRL,BSD,INR,BWP,BYR,BZD,CAD,CDF,CHW,CHF,CLP,CNY,COU,CRC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,EUR,FJD,FKP,GBP,GEL,GHS,GIP,GMD,GNF,GTQ,GYD,HKD,MOP,HNL,HRK,HUF,IDR,ILS,NPR,IQD,IRR,ISK,JMD,JOD,JPY,KES,KGS,THB,KMF,KPW,KRW,KWD,KYD,KZT,LBP,LKR,LRD,LSL,LYD,MAD,MDL,MGA,MKD,MNT,MRO,MUR,MVR,MWK,MXV,MYR,MZN,NAD,NGN,NIO,NOK,NZD,MOR,PEN,PGK,PHP,PKR,PLN,PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SHP,SLL,SOS,SRD,SSP,STD,SYP,SZL,TJS,TMT,TND,TOD,TRY,TTD,TWD,TZS,UAH,UGX,USN,ZWL,UYU,UZS,VEF,VND,VUV,WST,XAF,XCD,XOF,XPF,YER,ZAR,ZMW"
        #country_code by string
        # 볼리비아 기금부호(BOV) 제외 모든 화폐 단위 코드

        country_list_all = country_codes_all.split(",")
        # list 형태

        country_codes_major = "ARS,AUD,BRL,CAD,CNY,EUR,GBP,INR,JPY,KRW,PHP,SGD,TRY,USD"
        # 아르헨티나 페소, 오스트레일리아 달러, 브라질 헤알, 캐나다 달러, 중국 위안, 유로, 파운드 스털링, 일본 엔, 대한민국 원
        # 필리핀 페소, 싱가포르 달러, 터키 리라, 미국 달러
        # 주요 국가 화폐 단위 코드

        country_list_major = country_codes_major.split(",")
        # 주요 국가 화폐 단위 list 형태

        self.code_string = country_codes_major
        self.code_list = country_list_major
        self.APIUrl = "https://api.manana.kr/exchange/rate/"

        self.db = Database()

    def get_exchange_rate(self, src):
        response = requests.get(self.APIUrl + src + "/" + self.code_string + ".json")
        return response.json()

    def process_data(self, json_dict):
        tuple_list = []

        for dictData in json_dict:
            string = dictData['name']
            dct = string[:3]
            src = string[3:6]

            rate = round(dictData['rate'], 3)

            if src == dct or src == '=X':
                continue

            data = (src, dct, rate)
            tuple_list.append(data)

        return tuple_list

    def commit_data(self, currency_info):
        self.db.execute(query_formats.exchange_rate_delete % currency_info[0], currency_info[1])
        self.db.execute(query_formats.exchange_rate_insert_format % (currency_info[0], currency_info[1], currency_info[2]))
