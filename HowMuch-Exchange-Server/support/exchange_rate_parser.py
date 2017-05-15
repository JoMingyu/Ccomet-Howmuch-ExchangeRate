# -*- coding: utf-8 -*-

import requests
import datetime

from database import query_formats
from database import database
from firebase import fcm_sender
from support import stastic_data

class Parser:
    _instance = None

    def __new__(cls):
        # 싱글톤 패턴
        if not cls._instance:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        country_codes_all = "AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAM,USD,BDT,BGN,BHD,BIF,SGD,BRL,BSD,INR,BWP,BYR,BZD,CAD,CDF,CHW,CHF,CLP,CNY,COU,CRC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,EUR,FJD,FKP,GBP,GEL,GHS,GIP,GMD,GNF,GTQ,GYD,HKD,MOP,HNL,HRK,HUF,IDR,ILS,NPR,IQD,IRR,ISK,JMD,JOD,JPY,KES,KGS,THB,KMF,KPW,KRW,KWD,KYD,KZT,LBP,LKR,LRD,LSL,LYD,MAD,MDL,MGA,MKD,MNT,MRO,MUR,MVR,MWK,MXV,MYR,MZN,NAD,NGN,NIO,NOK,NZD,MOR,PEN,PGK,PHP,PKR,PLN,PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SHP,SLL,SOS,SRD,SSP,STD,SYP,SZL,TJS,TMT,TND,TOD,TRY,TTD,TWD,TZS,UAH,UGX,USN,ZWL,UYU,UZS,VEF,VND,VUV,WST,XAF,XCD,XOF,XPF,YER,ZAR,ZMW"
        # country_code by string
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

        self.db = database.Database()
        self.fcm_sender = fcm_sender.FCMSender('AAAAGhKg7Ws:APA91bGTOrM2nmAwP31NoY7DcbqD5ZpYzupJwUyOStM-TD7zk7jddIrzUAUlM5wXd5Jz94kbz-ab7uazV8UTxGe89H5aeyl5vudLCceeCbihjgTOGPDqX6fQK5FVMwKEZ-T3vgt7vLBM')

        self.last_average_date = datetime.date.today()

        self.section = 30
        self.exploit = stastic_data.ExploitRate('temp', 'temp')

    def get_exchange_rate(self, src):
        response = requests.get(self.APIUrl + src + "/" + self.code_string + ".json")
        return response.json()

    @staticmethod
    def process_data(json_dict):
        tuple_list = []

        for dictData in json_dict:
            string = dictData['name']
            src = string[:3]
            dst = string[3:6]

            rate = round(dictData['rate'], 3)

            if src == dst or dst == '=X':
                continue

            data = (src, dst, rate)
            tuple_list.append(data)

        return tuple_list

    def commit_data(self, exchange_rates, parse_count):
        for exchange_rate in exchange_rates:
            src_nation = exchange_rate[0]
            dst_nation = exchange_rate[1]
            new_rate = exchange_rate[2]

            rows = self.db.execute(query_formats.exchange_rate_select_format % (src_nation, dst_nation))
            # 기존 데이터

            self.db.execute(query_formats.exchange_rate_delete_format % (src_nation, dst_nation))
            self.db.execute(query_formats.exchange_rate_insert_format % (src_nation, dst_nation, new_rate))
            # 새로운 데이터 삽입

            if rows:
                # 기존 데이터가 이미 있었던 경우
                old_rate = rows[0]['exchange_rate']
                if old_rate != new_rate:
                    # 환율 변동이 있을 경우
                    self.fcm_sender.send(src_nation, dst_nation, old_rate, new_rate)
                    # fcm send

            average_rows = self.db.execute(query_formats.temp_exchange_rate_select_format % (src_nation, dst_nation))
            # 하루 단위 평균값 저장 임시 테이블
            if average_rows:
                # temp_exchange_rate에 데이터가 이미 있는 경우
                average = round((new_rate + average_rows[0]['exchange_rate']) / 2, 3)

                self.db.execute(query_formats.temp_exchange_rate_delete_format % (src_nation, dst_nation))
                self.db.execute(query_formats.temp_exchange_rate_insert_format % (src_nation, dst_nation, average))

                # 오늘 날짜를 구해서 만약 날짜가 지났다면 2000-00-00 형식으로 daily_exchange_rate 테이블에 값을 넣음
                temp = datetime.date.today()
                if temp.day != self.last_average_date.day:
                    self.db.execute(query_formats.daily_exchange_rate_insert_format %
                                    (src_nation, dst_nation, temp.strftime('%Y-%m-%d'), average))
                    
                    if src_nation in 'USD' and dst_nation in 'TRY':
                        self.last_average_date = temp
            else:
                # temp_exchange_rate에 데이터가 없는 경우
                self.db.execute(query_formats.temp_exchange_rate_insert_format % (src_nation, dst_nation, new_rate))