<template>
<div align="center">
    <div style="width:700px">
    <div class="flex">
        <div style="flex:6">Title : {{ article.title }}</div>
        <div style="flex:1">Views : {{ article.views }}</div>
    </div>
    <div class="flex">
        <div style="flex:1">Name : {{ article.user_name }}</div>
        <div style="flex:2">Date : {{ article.last_update }}</div>
    </div>
    <div style="min-height:200px;border:1px solid lightgray">
        <p>{{ article.artbody }}</p>
    </div>
    <div align="center" style="margin-top:20px">
        <button>Good</button>
        <button>bad</button>
    </div>
    <div class="flex" v-for="com in article.comlist" style="padding:5px" :key="com.body">
        <div style="flex:3">{{ com.name }}</div>
        <div style="flex:7">{{ com.body }}</div>
    </div>
    <div class="flex">
        <div style="flex:3">
        <input v-model="name" type="text" name="name" placeholder="Name" style="height:25px;width:110px;margin:6px"/>
        <input v-model="password" type="password" name="password" placeholder="Password" style="height:25px;width:110px;margin:6px"/>
        </div>
        <div style="flex:7">
        <textarea style="width:100%" v-model="combody"  rows="3" name="combody"></textarea>
        <button @click="comClick()" style="float:right;margin-top:10px">submit</button>
        </div>
    </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'
import { ip } from '../../helpers/ip'
export default {
    props:['id'],
    data() {
        return {
            article:{},
            user:null,
            name:null,
            password:null,
            combody:null,
        }
    },
    mounted() {
        axios.get(ip+'/api/article/id/'+this.id)
        .then(response=>{
            this.article=response.data
        })
        .catch(e=>{
            console.log(e)
        })
    },
    methods: {
        comClick() {
            var comData={}
            if(this.user){
            comData={
                'checkUser':true,'name':this.user.displayName,
                'userId':this.user.uid,'password':null,'body':this.combody}
            }else{
                comData={
                'checkUser':false,'name':this.name,
                'userId':null,'password':this.password,'body':this.combody}
            }
            if(this.user || (this.password!=null && this.name!=null)){
                axios.put(ip+'/api/article/addcom/'+this.article._id,{'comData':comData}
                )
                    .then(res => {
                        axios.get(ip+'/api/article/id/'+this.id)
                        .then(response=>{
                                this.article=response.data
                        })
                        .catch(e=>{
                            console.log(e)
                        }) 
                    })
                    .catch(e => {
                    console.log(e)
                    })   
            }
        }
    }

}
</script>

<style>
.flex {
    display: flex;
}
.flex div {
    border:1px solid lightgray;
    padding:5px
}
</style>