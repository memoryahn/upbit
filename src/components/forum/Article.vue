<template>
<div align="center">
    <div style="width:700px">
    <div class="flex">
        <div style="flex:6">Title : {{ gif.title }}</div>
        <div style="flex:1">Views : {{ gif.views }}</div>
    </div>
    <div class="flex">
        <div style="flex:1">Name : {{ gif.user_name }}</div>
        <div style="flex:2">Date : {{ gif.last_update }}</div>
    </div>
    <div style="border:1px solid lightgray">
        <p>{{ gif.artbody }}</p>
    </div>
    <div v-for="src in gif.srcs" style="padding:10px" :key="src">
        <img :src="src">
    </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'

export default {
    props:['id'],
    data() {
        return {
            gif:{}
        }
    },
    created() {
        axios.get('http://127.0.0.1:5000/api/article/id/'+this.id)
        .then(response=>{
            this.gif=response.data
        })
        .catch(e=>{
            console.log(e)
        })
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