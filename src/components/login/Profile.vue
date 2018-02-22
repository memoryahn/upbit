<template>
<div>
    <h1>Profile</h1>
    <!-- <p>{{ user.displayName }}</p> -->
    <!-- <p>{{ user.email }}</p> -->
    <!-- <img :src="user.pothoUrl"> -->
    <p>{{ name }}</p>
    <button @click="logout">logout</button>
</div></template>
<script>
import firebase from 'firebase'
export default {
    data() {
        return {
            user:{},
            name:''
        }
    },
    created() {
        this.user=firebase.auth().currentUser
        console.log(this.user)
        if(this.user){
            this.name = this.user.displayName
        }else{
            this.$router.push('/Auth')
        }
    },
    methods: {
        logout() {
            firebase.auth().signOut()
        }
    }

}</script>