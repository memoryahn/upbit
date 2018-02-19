from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import urllib.request
import json
from flask_cors import CORS
from datetime import datetime




app = Flask(__name__)
CORS(app)

app.config['MONGO_DBNAME'] = 'upbit'
app.config['MONGO_HOST'] = 'mongodb://220.230.124.148:27017'
app.config['MONGO_PORT'] = '27017'

mongo = PyMongo(app)
coin = [
{"name" :"비트코인"
,"code":"BTC"},

{"name" :"에이다"
,"code":"ADA"},

{"name" :"리플"
,"code":"XRP"},

{"name" :"비트코인캐시"
,"code":"BCC"},

{"name" :"이더리움"
,"code":"ETH"},

{"name" :"퀀텀"
,"code":"QTUM"},

{"name" :"네오"
,"code":"NEO"},

{"name" :"뉴이코노미무브먼트"
,"code":"XEM"},

{"name" :"스테이터스네트워크토큰"
,"code":"SNT"},

{"name" :"리스크"
,"code":"LSK"},

{"name" :"스텔라루멘"
,"code":"XLM"},

{"name" :"라이트코인"
,"code":"LTC"},

{"name" :"이더리움클래식"
,"code":"ETC"},

{"name" :"스팀달러"
,"code":"SBD"},

{"name" :"스팀"
,"code":"STEEM"},

{"name" :"비트코인골드"
,"code":"BTG"},

{"name" :"어거"
,"code":"REP"},

{"name" :"아더"
,"code":"ARDR"},

{"name" :"메탈"
,"code":"MTL"},

{"name" :"웨이브"
,"code":"WAVES"},

{"name" :"머큐리"
,"code":"MER"},

{"name" :"오미세고"
,"code":"OMG"},

{"name" :"스트라티스"
,"code":"STRAT"},

{"name":"파워렛저"
,"code":"POWR"},

{"name" :"블록틱스"
,"code":"TIX"},

{"name" :"아인스타이늄"
,"code":"EMC2"},

{"name" :"피벡스"
,"code":"PIVX"},

{"name" :"스토리지"
,"code":"STORJ"},

{"name" :"코모도"
,"code":"KMD"},

{"name" :"그로스톨코인"
,"code":"GRS"},

{"name" :"모네로"
,"code":"XMR"},

{"name" :"아크"
,"code":"ARK"},

{"name" :"버트코인"
,"code":"VTC"},

{"name" :"지캐시"
,"code":"ZEC"},

{"name" :"대시"
,"code":"DASH"},
]


@app.route('/',methods=['GET'])
def get_data():
    data=[]
    count=0
    for code in coin:
        url='https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.KRW-'+code['code']+'&count=1'
        headersObject = { 'User-Agent': '', 'Accept': '*/*' }
        with urllib.request.urlopen(urllib.request.Request(url, headers = headersObject)) as coinUrl:
            coinData = coinUrl.read()
            encoding = coinUrl.info().get_content_charset('utf-8')    
            tradePrice=json.loads(coinData.decode(encoding))[0]['tradePrice']
            candleDateTimeKst=json.loads(coinData.decode(encoding))[0]['candleDateTimeKst']
            openingPrice=json.loads(coinData.decode(encoding))[0]['openingPrice']
            highPrice=json.loads(coinData.decode(encoding))[0]['highPrice']
            lowPrice=json.loads(coinData.decode(encoding))[0]['lowPrice']
        result={'name':code['name'],'code':code['code'],
        "tradePrice":tradePrice,
        "candleDateTimeKst": candleDateTimeKst,
        "openingPrice": openingPrice,
        "highPrice": highPrice, 
        "lowPrice": lowPrice,        
        }
        data.append(result)
        count=count+1
    tempdate = data[0]['candleDateTimeKst'].replace("+09:00","")
    d =datetime.strptime(tempdate ,'%Y-%m-%dT%H:%M:%S')
    print(d.hour)
    return jsonify(data)
@app.route('/api/open',methods=['GET'])
def get_open():
    data=[]
    for code in coin:
        url='https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/60?code=CRIX.UPBIT.KRW-'+code['code']+'&count=24'
        headersObject = { 'User-Agent': '', 'Accept': '*/*' }
        with urllib.request.urlopen(urllib.request.Request(url, headers = headersObject)) as coinUrl:
            coinData = coinUrl.read()
            encoding = coinUrl.info().get_content_charset('utf-8')    
            for i in json.loads(coinData.decode(encoding)):
                candleDateTimeKst = i['candleDateTimeKst']
                tempdate = candleDateTimeKst.replace("+09:00","")
                d =datetime.strptime(tempdate ,'%Y-%m-%dT%H:%M:%S')
                if d.hour == 7:
                    openingPrice=i['openingPrice']
        result={'name':code['name'],'code':code['code'],'open':openingPrice}
        data.append(result)
    return jsonify(data)


if __name__=='__main__':
    app.run(debug=True)

