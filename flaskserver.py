from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'upbit'
app.config['MONGO_HOST'] = 'mongodb://220.230.124.148:27017'
app.config['MONGO_PORT'] = '27017'

mongo = PyMongo(app)

@app.route('/api/data',methods=['POST'])
def get_data():
    # urlltc='https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.KRW-LTC&count=1'
    # headersObject = { 'User-Agent': '', 'Accept': '*/*' }
    # with urllib.request.urlopen(urllib.request.Request(urlbtc, headers = headersObject)) as btcUrl:
    #     btcData = btcUrl.read()
    #     encoding = btcUrl.info().get_content_charset('utf-8')    
    #     upbitBtc=json.loads(btcData.decode(encoding))[0]['tradePrice']
    return 'data'