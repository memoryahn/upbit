<template>
<div align="center">
    <div style="width:700px">
        <div style="margin-top:10px" class="flex">
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
        <div style="flex:6;text-align:left" @click="artClick(article._id)">{{ article.title }} <span style="color:red">[{{ article.comCount }}]</span></div>        
        <div style="flex:1">{{ article.user_name }}</div> 
        <div style="flex:0.7">{{ article.last_update }}</div>
        <div style="flex:0.7">{{ article.views }}</div> 
        </div>
    </div>
    <div style="width:700px">
        <div style="margin-top:10px;font-size:13px" class="flex">
        <div style="flex:1"> ◀ </div>
        <div style="flex:1">1</div>
        <div style="flex:1">2</div>
        <div style="flex:1">3</div>
        <div style="flex:1">4</div>
        <div style="flex:1">5</div>
        <div style="flex:1">6</div>
        <div style="flex:1">7</div>
        <div style="flex:1">8</div>
        <div style="flex:1">▶</div>
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
export default {
    data() {
        return {
            articles:{},
        }
    },
    methods: {
        artClick(id) {
            this.$router.push('/Forum/id/'+id)
        },
        newArticle() {
            this.$router.push('/Forum/new')
        }
    },
    created() {
        axios.get('http://127.0.0.1:5000/api/article/page/1')
            .then(response => {
                for(var r in response.data){
                    var temptime = new Date(response.data[r].last_update)
                    var temptime_hour = temptime.getUTCHours()
                    var temptime_min = temptime.getUTCMinutes()
                    var tt = temptime_hour+":"+temptime_min
                    if(response.data[r].comlist==null){
                    response.data[r].comCount=0
                    }else{
                    response.data[r].comCount=Object.keys(response.data[r].comlist).length
                    }
                    response.data[r].last_update = tt
                }        
                for(var i in response.data){
                    Vue.set(this.articles,i,response.data[i])
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