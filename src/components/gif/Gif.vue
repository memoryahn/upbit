<template>
<div align="center">
    <div style="width:700px">
    <div class="flex borderbot padding">
        <div align="left" style="flex:6;font-size:18px;padding-top:5px;margin-left:20px">{{ gif.title }}</div>
        <div class="flex:3">
        <div class="flex">
        <div align="left" style="flex:1"> {{ gif.author }}</div>
        <div align="right" style="flex:1">조회수 : {{ gif.views }}</div>
        </div>
        <div align="right" style="flex:2;font-size:12px">{{ gif.last_update }}</div>
        </div>
    </div>
    <div style="background-color:#fafafa">
    <div v-for="src in gif.srcs" style="padding:10px" :key="src">
        <img :src="src">
    </div>
    <div class="border" align="center" style="margin-top:20px;padding-bottom:10px">
        <button class="btn" style="width:70px">좋아요</button>
        <button class="btn bgred" style="width:70px">싫어요</button>
    </div>
    </div>
    <div class="flex padding" style="margin-bottom:10px" v-for="com in gif.comlist" :key="com.body">
        <div style="flex:2;border:1px solid #e8e8e8;height:20px;
        border-radius:20px;padding:10px;background-color:#fafafa">{{ com.name }}</div>
        <div align="left" style="flex:8;width:400px;border:1px solid #e8e8e8;
        border-radius:20px;padding:10px;background-color:#fafafa;
        margin-left:20px;font-size:14px;white-space: pre-line">{{ com.body }}</div>
        <div style="flex-grow:2"></div>
    </div>

    <div class="flex borderboth padding" style="background-color:#fafafa;border-radius:10px">
        <div style="flex:2;border-right:1px solid #e8e8e8">
        <input v-model="name" type="text" name="name" placeholder="Name" style="height:24px;width:110px;"/>
        <input v-model="password" type="password" name="password" placeholder="Password" style="height:24px;width:110px;margin:6px"/>
        </div>
        <div style="flex:8;padding-left:20px;padding-right:10px">
        <textarea style="width:98%;padding:5px;border-radius:5px" v-model="combody"  rows="4" name="combody"></textarea>
        <button v-if="combody=='' || name=='' || password==''" class="btn bggray" style="float:right;margin-top:10px">댓글</button>       
        <button v-if="combody!='' && name!='' && password!=''" class="btn bgblue" @click="comClick()" style="float:right;margin-top:10px">댓글</button>
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
            name:'',
            password:'',
            combody:'',
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
            if(this.user || (this.password!='' && this.name!='' && this.combody!='' )){
                axios.put(ip+'/api/gif/addcom/'+this.gif._id,{'comData':comData}
                )
                    .then(res => {
                        axios.get(ip+'/api/gif/id/'+this.id)
                        .then(response=>{
                                this.gif=response.data
                                this.combody=''
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

<style scoped>
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
    border:1px solid lightgray;
}

</style>