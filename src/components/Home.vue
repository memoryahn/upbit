<template>
<div style="padding:20px">
<div align="center" class="row" style="margin-top:10px">
  <div>
    <div align="left">총코인 : 35</div>
    <div>+5% 코인 : {{ count }}</div>
  </div>
<div class="col-12">
    <div class="row" style="font-size:10px">
      <div class="title col-2">이름</div>
      <div class="title col-1">코드</div>
      <div class="title col-1">OPEN 가격</div>
      <div class="title col-1">현재 가격</div>
      <div class="title col-1">상승률</div>
      <div class="title col-1">최고</div>
      <div class="title col-1">최저</div>
      <div class="title col-1">순위</div>
      <div class="title col-3">그래프</div>
    </div>
  <div class="row" style="font-size:10px" v-for="(d,i) in data" :key="i">
    <div align="left" class="col-2" style=";border:1px solid lightgray">
    {{ d.name }}
    </div>
    <div class="col-1" style=";border:1px solid lightgray">
    {{ d.code }}
    </div>
    <div align="right" class="col-1" style=";border:1px solid lightgray">
    {{ comma(d.open) }}
    </div>
    <div align="right" class="col-1" style=";border:1px solid lightgray">
    {{ comma(d.tradePrice) }}
    </div>
    <div align="left" v-if="d.climeRate >= 5" class="col-1" 
      style="color:red;border:1px solid lightgray">▲ {{ d.climeRate }}%</div>
    <div align="left" v-if="d.climeRate < 5" class="col-1" 
      style="color:blue;border:1px solid lightgray">▼ {{ d.climeRate }}%</div>
    <div class="col-1" style="color:red;border:1px solid lightgray">▲ +15%</div>
    <div class="col-1" style="color:blue;border:1px solid lightgray">▼ -10%</div>
    <div class="col-1" style="color:red;border:1px solid lightgray">( {{ d.rate }} )</div>
    <div class="col-3" style=";border:1px solid lightgray">[     |      ]</div>
  </div>
</div>
          </div> 
</div>
</template>
<script>
import axios from 'axios'
import Vue from 'vue'


export default {
  data() {
    return {
      data:{},
      count:0
    }
  },
  methods: {
    comma(nStr){
      nStr += '';
      var x = nStr.split('.');
      var x1 = x[0];
      var x2 = x.length > 1 ? '.' + x[1] : '';
      var rgx = /(\d+)(\d{3})/;
      while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + ',' + '$2');
      }
      return x1 + x2;
    },
    stop() {
    },
    getdata() {
       axios.get('http://127.0.0.1:5000')
    .then(response=>{
      console.log('connect')
      this.data1=response.data

    })
    .catch(e=>{
      console.log(e)
    })
      
    }
  },
  created() {
    axios.get('http://127.0.0.1:5000/api/open')
    .then(response=>{
      console.log('connect')
      this.data=response.data
      axios.get('http://127.0.0.1:5000')
    .then(response=>{
      console.log('connect2')
      this.count=0
      for(let i in this.data){
        for(let k in response.data){
        if(this.data[i].code==response.data[k].code){
          this.data[i].tradePrice=response.data[k].tradePrice
          Vue.set(this.data[i],'climeRate',(((this.data[i].tradePrice-this.data[i].open)/this.data[i].open)*100).toFixed(2))
          if(this.data[i].climeRate>=5){
            this.count++
          }
        }
        }
      }
      this.data.sort(function(b, a){return a.climeRate - b.climeRate});
      for(let i in this.data){
      Vue.set(this.data[i],'rate',Number(i)+1)
      }
    })
    .catch(e=>{
      console.log(e)
    })
      // for(let i in this.data){
      //   this.data[i].open=addCommas(this.data[i].open)
      // }
    })
    .catch(e=>{
      console.log(e)
    })

    
    
  }
}
</script>
<style>
.title {
  border:1px solid lightgray;
  color:brown;
}
</style>