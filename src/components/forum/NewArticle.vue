<template>
<div align="center">
    <div style="width:700px">
        <input v-model="title" type="text" name="title" placeholder="Title" style="height:25px;width:100%"/>
        <textarea style="width:100%" v-model="artbody"  placeholder="Body" rows="3" name="artbody"></textarea>
        <input v-model="name" type="text" name="name" placeholder="Name" style="height:25px;width:110px;margin:6px"/>
        <input v-model="password" type="password" name="password" placeholder="Password" style="height:25px;width:110px;margin:6px"/>
        <button @click="newClick()" style="float:right;margin-top:10px">submit</button>
    </div>
</div>
</template>
<script>
import axios from 'axios'
import { ip } from '../../helpers/ip'
export default {
    data() {
        return {
            title:null,
            name:null,
            password:null,
            artbody:null,
            
        }
    },
    methods: {
        newClick() {
            var articleData = {
                'title':this.title,
                'artbody':this.artbody,
                'user_name':this.name,
                'user_id':'',
                'password':this.password,
                'like':0,
                'bad':0,
                'views':0,
            }
            axios.post(ip+'/api/article/new',articleData)
            .then(response=>{
                console.log(response.data)
                this.$router.push('/forum')
            })
            .catch(e=>{
                console.log(e)
            })
        }
    }
}
</script>
<style scoped>
.flex {
    display:flex;
}
</style>