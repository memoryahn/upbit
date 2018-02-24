<template>
<div align="center">
  <div class="flex" style="width:700px;margin-top:10px;font-size:12px" >
    <div class="info" style="flex:1">총코인 : 35</div>
    <div class="info" style="flex:1">+3% 코인 : {{ count }}</div>
    <div class="info" style="flex:1">+ 코인 : {{ upcount }}</div>
    <div style="flex:4"></div>
  </div>
  <div style="width:700px;font-size:12px">
    <div class="flex">
      <div class="title" style="flex:2">이름</div>
      <div class="title" style="flex:0.7">코드</div>
      <div class="title" style="flex:1">7시 open가격</div>
      <div class="title" style="flex:1">현재 가격</div>
      <div class="title" style="flex:1">상승률</div>
      <div class="title" style="flex:1">최고</div>
      <div class="title" style="flex:1">최저</div>
      <div class="title" style="flex:0.5">순위</div>
    </div>
    <div id="dd" class="flex" style="font-size:12px" 
    v-for="(d,i) in data" :key="i"
    v-if="!loading">
      <div class="data" style="flex:2;color:red" align="left" v-if="i<=14">{{ d.name }}</div>
      <div class="data" style="flex:2" align="left" v-if="i>14">{{ d.name }}</div>
      <div class="data" style="flex:0.7" >{{ d.code }}</div>
      <div class="data" style="flex:1" align="right">{{ comma(d.openingPrice) }}</div>
      <div class="data" style="flex:1" align="right">{{ comma(d.tradePrice) }}</div>
      <div class="data" style="flex:1;color:red;"  v-if="d.climeRate >= 0" >▲ {{ d.climeRate }}%</div>
      <div class="data" style="flex:1;color:blue;"  v-if="d.climeRate < 0" >▼ {{ d.climeRate }}%</div>
      <div class="data" style="flex:1;color:red;" v-if="d.highRate >=5">{{ d.highRate }}%</div>
      <div class="data" style="flex:1;" v-if="d.highRate <5">{{ d.highRate }}%</div>
      <div class="data" style="flex:1" >{{ d.lowRate }}%</div>
      <div class="data" style="flex:0.5;color:red;" v-if="d.climeRate >= 3" >( {{ d.rate }} )</div>
      <div class="data" style="flex:0.5;color:blue;" v-if="d.climeRate < 3" >( {{ d.rate }} )</div>
    </div>
      <div v-if="loading">
        <h1>Loading</h1>
      </div>
  </div>
</div> 
</template>
<script>
import axios from 'axios'
import Vue from 'vue'
import { ip } from '../helpers/ip'
var tim

export default {
  data() {
    return {
      data:{},
      count:0,
      upcount:0,
    }
  },
  computed : {
    loading(){
      return this.$store.getters.loading
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
      axios.get(ip+'/api/open')
      .then(response=>{
      console.log('connect')
      this.data=response.data
      this.count=0
      this.upcount=0
      for(let i in this.data){
          Vue.set(this.data[i],'climeRate',(((this.data[i].tradePrice-this.data[i].openingPrice)/this.data[i].openingPrice)*100).toFixed(2))
          Vue.set(this.data[i],'highRate',(((this.data[i].highPrice-this.data[i].openingPrice)/this.data[i].openingPrice)*100).toFixed(2))
          Vue.set(this.data[i],'lowRate',(((this.data[i].lowPrice-this.data[i].openingPrice)/this.data[i].openingPrice)*100).toFixed(2))
          if(this.data[i].climeRate>=3){
            this.count++
          }
          if(this.data[i].climeRate>=0){
            this.upcount++
          }
      }
      this.data.sort(function(b, a){return a.climeRate - b.climeRate});
      for(let i in this.data){
      Vue.set(this.data[i],'rate',Number(i)+1)
      }
      this.$store.dispatch('setLoading',false)
    })
    .catch(e=>{
      console.log(e)
      this.$store.dispatch('setLoading',false)
    })   
    }
  },
  mounted() {
  this.$store.dispatch('setLoading',true)
  this.getdata()
  tim=setInterval(function() {this.getdata()}.bind(this),10000)    
  },
  destroyed() {
    clearInterval(tim)
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
#dd:nth-child(odd){
  background: #eee;
}
</style>