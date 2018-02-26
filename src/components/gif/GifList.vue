<template>
<div align="center">
    <div style="width:700px">
        <div style="margin-top:10px;font-size:14px" class="flex border">
        <div style="flex:1">Num</div>
        <div style="flex:6">Title</div>        
        <div style="flex:1">Author</div> 
        <div style="flex:0.7">Date</div>
        <div style="flex:0.7">Views</div> 
        </div>
    </div>
    <div style="width:700px;font-size:12px">
        <div id="list" class="flex border" v-for="gif in gifs" :key="gif._id">
        <div style="flex:1">{{ gif.count }}</div>
        <div style="flex:6;text-align:left" @click="artClick(gif._id)">{{ gif.title }} <span style="color:red" v-if="gif.comCount > 0">[{{ gif.comCount }}]</span></div>        
        <div style="flex:1">{{ gif.author }}</div> 
        <div style="flex:0.7">{{ gif.last_update }}</div>
        <div style="flex:0.7">{{ gif.views }}</div> 
        </div>
    </div>
    <div style="width:600px">
        <div style="margin-top:10px;font-size:13px" class="flex">
        <div style="flex:2" @click="pre"> ◀ Prev</div>
        <div @click="pageClick(i)" :id="i" style="flex:1" v-for="i in page" :key="i">{{ i }}</div>
        <div style="flex:2" @click="next">Next ▶</div>
        </div>
    </div>
    <div style="width:700px;margin-top:10px;justify-content: flex-end" class="flex">
        <div style="flex-grow:8"></div>
        <div style="flex:2">search</div>
        <div style="flex-grow:4"></div>
        <div style="flex:2">new</div>
    </div>
</div>
</template>
<script>
import axios from 'axios'
import Vue from 'vue'
import { ip } from '../../helpers/ip'
export default {
    data() {
        return {
            gifs:{},
            page:[],
        }
    },
    methods: {
        artClick(id) {
            axios.put(ip+'/api/gif/views/'+id)
            .then(response => { 
            })
            .catch(e => {
            console.log(e)
            })
            this.$router.push('/Gif/'+id)
        },
        pre() {
            if(this.page[0]>10){
            for(let i in this.page){
                Vue.set(this.page,i,this.page[i]-10)
            }
            }
        },
        next() {
            for(let i in this.page){
                Vue.set(this.page,i,this.page[i]+10)
            }
        },
        pageClick(id) {
            axios.get(ip+'/api/gif/page/'+id)
            .then(response => {
                for(var r in response.data){
                    var temptime = new Date(response.data[r].last_update)
                    var temptime_hour = temptime.getUTCHours()
                    var temptime_min = temptime.getUTCMinutes()
                    if(temptime_min == 0){
                        temptime_min='00'
                    }
                    var tt = temptime_hour+":"+temptime_min
                    if(response.data[r].comlist==null){
                    response.data[r].comCount=0
                    }else{
                    response.data[r].comCount=Object.keys(response.data[r].comlist).length
                    }
                    response.data[r].last_update = tt
                }        
                for(var i in response.data){
                    Vue.set(this.gifs,i,response.data[i])
                }
            })
            .catch(e => {
            console.log(e)
            })
        }
    },
    mounted() {
        for(let i=0;i<10;i++){
            this.page[i]=i+1
        }
        axios.get(ip+'/api/gif/page/1')
            .then(response => {
                for(var r in response.data){
                    var temptime = new Date(response.data[r].last_update)
                    var temptime_hour = temptime.getUTCHours()
                    var temptime_min = temptime.getUTCMinutes()
                    if(temptime_min == 0){
                        temptime_min='00'
                    }
                    var tt = temptime_hour+":"+temptime_min
                    if(response.data[r].comlist==null){
                    response.data[r].comCount=0
                    }else{
                    response.data[r].comCount=Object.keys(response.data[r].comlist).length
                    }
                    response.data[r].last_update = tt
                }        
                for(var i in response.data){
                    Vue.set(this.gifs,i,response.data[i])
                }
            })
            .catch(e => {
            console.log(e)
            })
    }
}
</script>
<style scoped>
#list:nth-child(odd) {
    background: #eee
}
.flex {
    display:flex;
}
.padding {
    padding: 5px
}
.border {
    border-bottom:1px solid lightgray;
    padding: 5px
}
</style>