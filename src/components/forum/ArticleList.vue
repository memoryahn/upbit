<template>
<div align="center">
    <div style="width:700px">
        <div style="margin-top:10px;font-size:12px" class="flex">
        <div style="flex:1">Num</div>
        <div style="flex:6">Title</div>        
        <div style="flex:1">Author</div> 
        <div style="flex:0.7">Date</div>
        <div style="flex:0.7">Views</div> 
        </div>
    </div>
    <div style="width:700px;font-size:12px">
        <div id="list" class="flex" v-for="article in articles" :key="article._id">
        <div style="flex:1">{{ article.articleNumber }}</div>
        <div style="flex:6;text-align:left" @click="artClick(article._id)">{{ article.title }} <span style="color:red" v-if="article.comCount > 0">[{{ article.comCount }}]</span></div>        
        <div style="flex:1">{{ article.user_name }}</div> 
        <div style="flex:0.7">{{ article.update }}</div>
        <div style="flex:0.7">{{ article.views }}</div> 
        </div>
    </div>
    <div style="width:700px">
        <div style="margin-top:10px;font-size:13px" class="flex">
        <div style="flex:1" @click="pre"> ◀ </div>
        <div @click="pageClick(i)" :id="i" style="flex:1" v-for="i in page" :key="i">{{ i }}</div>
        <div style="flex:1" @click="next">▶</div>
        </div>
    </div>
    <div style="width:700px;margin-top:10px;justify-content: flex-end" class="flex">
        <div style="flex-grow:8"></div>
        <div style="flex:2">search</div>
        <div style="flex-grow:4"></div>
        <div @click="newArticle" style="flex:2">new</div>
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
            articles:{},
            page:[],
        }
    },
    methods: {
        artClick(id) {
            axios.put(ip+'/api/article/views/'+id)
            .then(response => { 
            })
            .catch(e => {
            console.log(e)
            })
            this.$router.push('/Forum/id/'+id)
        },
        newArticle() {
            this.$router.push('/Forum/new')
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
            axios.get(ip+'/api/article/page/'+id)
            .then(response => {
                this.articles = response.data
                for(var i in this.articles){
                    var temptime = new Date(this.articles[i].last_update)
                    var temptime_hour = temptime.getUTCHours()
                    var temptime_min = temptime.getUTCMinutes()
                    if(temptime_min == 0){
                        temptime_min='00'
                    }
                    var tt = temptime_hour+":"+temptime_min
                    if(this.articles[i].comlist==null){
                    Vue.set(this.articles[i],'comCount',0)
                    }else{
                    Vue.set(this.articles[i],'comCount',Object.keys(this.articles[i].comlist).length)
                    }
                    Vue.set(this.articles[i],'update',tt)
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
        axios.get(ip+'/api/article/page/1')
            .then(response => {
                this.articles = response.data
                for(var i in this.articles){
                    var temptime = new Date(this.articles[i].last_update)
                    var temptime_hour = temptime.getUTCHours()
                    var temptime_min = temptime.getUTCMinutes()
                    if(temptime_min == 0){
                        temptime_min='00'
                    }
                    var tt = temptime_hour+":"+temptime_min
                    if(this.articles[i].comlist==null){
                    Vue.set(this.articles[i],'comCount',0)
                    }else{
                    Vue.set(this.articles[i],'comCount',Object.keys(this.articles[i].comlist).length)
                    }
                    Vue.set(this.articles[i],'update',tt)
                }        
            })
            .catch(e => {
            console.log(e)
            })
    }
}
</script>
<style>
#list:nth-child(odd) {
    background: #eee
}
.flex {
    display:flex;
}
.flex div {
    border: 1px solid lightgray;
    padding: 5px
}
</style>