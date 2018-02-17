<template>
<div>
  <h1>upbit</h1>
  <button class="btn" @click="getdata">get</button>
  <button class="btn" @click="stop">stop</button>
</div>
</template>
<script>
import axios from 'axios'
import Vue from 'vue'
var sockjs = new SockJS("https://crix-websocket.upbit.com/sockjs")
export default {
  data() {
    return {
      data:[],
      inter:null,
      count:1,
    }
  },
  methods: {
    stop() {
      sockjs.close()
  },
    getdata() {
      
  }
  },
  created() {
    console.log('get')
      sockjs.onopen = function () {
        console.log("Socket open")
        var s = [
          {
            ticket: "ram macbook"
          },
          {
            type: "recentCrix",
            codes: ["CRIX.UPBIT.KRW-BTC"]
            //codes: ["CRIX.UPBIT.KRW-BTC", "CRIX.BITFINEX.USD-BTC", "CRIX.BITFLYER.JPY-BTC", "CRIX.OKCOIN.CNY-BTC", "CRIX.KRAKEN.EUR-BTC", "CRIX.UPBIT.KRW-DASH", "CRIX.UPBIT.KRW-ETH", "CRIX.UPBIT.KRW-NEO", "CRIX.UPBIT.KRW-BCC", "CRIX.UPBIT.KRW-MTL", "CRIX.UPBIT.KRW-LTC", "CRIX.UPBIT.KRW-STRAT", "CRIX.UPBIT.KRW-XRP", "CRIX.UPBIT.KRW-ETC", "CRIX.UPBIT.KRW-OMG", "CRIX.UPBIT.KRW-SNT", "CRIX.UPBIT.KRW-WAVES", "CRIX.UPBIT.KRW-PIVX", "CRIX.UPBIT.KRW-XEM", "CRIX.UPBIT.KRW-ZEC", "CRIX.UPBIT.KRW-XMR", "CRIX.UPBIT.KRW-QTUM", "CRIX.UPBIT.KRW-LSK", "CRIX.UPBIT.KRW-STEEM", "CRIX.UPBIT.KRW-XLM", "CRIX.UPBIT.KRW-ARDR", "CRIX.UPBIT.KRW-KMD", "CRIX.UPBIT.KRW-ARK", "CRIX.UPBIT.KRW-STORJ", "CRIX.UPBIT.KRW-GRS", "CRIX.UPBIT.KRW-VTC", "CRIX.UPBIT.KRW-REP", "CRIX.UPBIT.KRW-EMC2", "CRIX.UPBIT.KRW-ADA", "CRIX.UPBIT.KRW-SBD", "CRIX.UPBIT.KRW-TIX", "CRIX.UPBIT.KRW-POWR", "CRIX.UPBIT.KRW-MER", "CRIX.UPBIT.KRW-BTG", "CRIX.COINMARKETCAP.KRW-USDT"]
          },
          {
            type: "crixTrade",
            codes: ["CRIX.UPBIT.KRW-BTC"]
          },
          {
            type: "crixOrderbook",
            codes: ["CRIX.UPBIT.KRW-BTC"]
          }
        ];
        sockjs.send(JSON.stringify(s));
        sockjs.onmessage = function (e) {
          console.log(JSON.parse(e.data))
          sockjs.close()
        }
      }
  }
}</script>