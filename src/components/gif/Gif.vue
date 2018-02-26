<template>
<div align="center">
    <div style="width:700px">
    <div class="flex borderbot padding">
        <div align="left" style="flex:6;font-size:18px;padding-top:5px">{{ gif.title }}</div>
        <div class="flex:3">
        <div class="flex">
        <div align="left" style="flex:1">{{ gif.author }}</div>
        <div align="right" style="flex:1">views : {{ gif.views }}</div>
        </div>
        <div align="right" style="flex:2;font-size:12px">{{ gif.last_update }}</div>
        </div>
    </div>
    <div v-for="src in gif.srcs" style="padding:10px" :key="src">
        <img :src="src">
    </div>
    <div class="border" align="center" style="margin-top:20px;padding-bottom:10px">
        <button>Good</button>
        <button>bad</button>
    </div>
    <div class="flex borderboth padding" style="background-color:#fafafa;margin-bottom:10px" v-for="com in gif.comlist" :key="com.body">
        <div style="flex:2;border-right:1px solid #e8e8e8">{{ com.name }}</div>
        <div align="left" style="flex:8;padding-left:20px">{{ com.body }}</div>
    </div>
    <div class="flex borderboth padding" style="background-color:#fafafa">
        <div style="flex:2;border-right:1px solid #e8e8e8">
        <input v-model="name" type="text" name="name" placeholder="Name" style="height:24px;width:110px;"/>
        <input v-model="password" type="password" name="password" placeholder="Password" style="height:24px;width:110px;margin:6px"/>
        </div>
        <div style="flex:8;padding-left:20px">
        <textarea style="width:98%;" v-model="combody"  rows="4" name="combody"></textarea>
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
            gif:{},
            user:null,
            name:null,
            password:null,
            combody:null,
        }
    },
    mounted() {
        axios.get(ip+'/api/gif/id/'+this.id)
        .then(response=>{
            this.gif=response.data
            console.log(this.gif)
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
                axios.put(ip+'/api/gif/addcom/'+this.gif._id,{'comData':comData}
                )
                    .then(res => {
                        axios.get(ip+'/api/gif/id/'+this.id)
                        .then(response=>{
                                this.gif=response.data
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
.padding {
    padding:5px
}
.borderbot {
    border-bottom:1px solid lightgray;
}
.borderboth {
    border-bottom:1px solid lightgray;
    border-top:1px solid lightgray;
}
</style>