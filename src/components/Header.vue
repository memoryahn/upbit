<template>
<div align="center" >
    <div style="background: lightslategrey;">
    <div class="flex" style="width:700px">
        <div @click="upbit">UPBIT</div>
        <div @click="gif">GIF</div>
        <!-- <div @click="forum">FORUM</div> -->
        <div style="flex-grow:5"></div>
        <!-- <div @click="login">LOGIN</div> -->
    </div>
    </div>    
</div>
</template>

<script>
export default {
    data() {
        return {

        }
    },
    methods: {
        upbit() {
            this.$router.push('/')
        },
        gif() {
            this.$router.push('/Gif')
        },
        forum() {
            this.$router.push('/Forum')
        },
        login() {
            this.$router.push('/Auth')
        }
    }
}
</script>

<style scoped>
.flex {
    display: flex;
    background: gray;
}
.flex div{
    background:lightslategrey;
    color: lightgray;
    font-size:20px;
    flex:1;
    padding:10px
}
.flex div:hover {
    cursor: pointer;
    color:black;
}
</style>