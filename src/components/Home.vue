<template>
<div style="padding:20px">
<div align="center">
  <div class="flex" style="width:700px" >
    <div class="info">총코인 : 35</div>
    <div class="info">+5% 코인 : {{ count }}</div>
    <div class="info">+ 코인 : {{ upcount }}</div>
  </div>
  <div style="width:700px;font-size:12px">
    <div class="flex">
      <div class="title" style="width:20%">코드</div>
      <div class="title" style="width:10%">이름</div>
      <div class="title" style="width:10%">OPEN 가격</div>
      <div class="title" style="width:10%">현재 가격</div>
      <div class="title" style="width:10%">상승률</div>
      <div class="title" style="width:10%">최고</div>
      <div class="title" style="width:10%">최저</div>
      <div class="title" style="width:10%">순위</div>
    </div>
    <div class="flex" style="font-size:10px" v-for="(d,i) in data" :key="i">
      <div class="data" style="width:20%" align="left">{{ d.name }}</div>
      <div class="data" style="width:10%" >{{ d.code }}</div>
      <div class="data" style="width:10%" align="right">{{ comma(d.open) }}</div>
      <div class="data" style="width:10%" align="right">{{ comma(d.tradePrice) }}</div>
      <div class="data" style="width:10%;color:red;" align="left" v-if="d.climeRate >= 0" >▲ {{ d.climeRate }}%</div>
      <div class="data" style="width:10%;color:blue;" align="left" v-if="d.climeRate < 0" >▼ {{ d.climeRate }}%</div>
      <div class="data" style="width:10%" >▲ +15%</div>
      <div class="data" style="width:10%" >▼ -10%</div>
      <div class="data" style="width:10%;color:red;" v-if="d.climeRate >= 5" >( {{ d.rate }} )</div>
      <div class="data" style="width:10%;color:blue;" v-if="d.climeRate < 5" >( {{ d.rate }} )</div>
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
      count:0,
      upcount:0,
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
      this.upcount=0
      for(let i in this.data){
        for(let k in response.data){
        if(this.data[i].code==response.data[k].code){
          this.data[i].tradePrice=response.data[k].tradePrice
          Vue.set(this.data[i],'climeRate',(((this.data[i].tradePrice-this.data[i].open)/this.data[i].open)*100).toFixed(2))
          if(this.data[i].climeRate>=5){
            this.count++
          }
          if(this.data[i].climeRate>=0){
            this.upcount++
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
.flex {
  display: flex
}
.info {
  border: 1px solid lightgray;
  color: green;
  padding: 5px
}
.title {
  border: 1px solid lightgray;
  color: brown;
  padding: 5px
}
.data {
  border: 1px solid lightgray;
  padding: 5px
}
</style>