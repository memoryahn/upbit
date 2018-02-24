import Vue from 'vue'
import App from './App'
import router from './router'
import { config } from './helpers/firebaseConfig'
import firebase from 'firebase'
import firebaseui from 'firebaseui'
import { store } from './store/store'
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  created() {
    firebase.initializeApp(config)
    firebase.auth().onAuthStateChanged((user)=>{
      if(user){
        // this.$router.push('/Profile')
      }else{
        // this.$router.push('/Auth')
      }
    })
  },
  render: h => h(App)
})
