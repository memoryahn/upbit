import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
// import * as firebase from 'firebase'
import router from '../router/index'

Vue.use(Vuex)



export const store = new Vuex.Store({
    state: {
        loading: false,
    },
  
    getters : {
        loading (state) {
            return state.loading
        },
    },
    mutations : {
        setLoadingM(state, arg) {
            state.loading = arg
        },
    },
    actions : {
        setLoading({commit},arg){
            commit('setLoadingM',arg)
        }
    }
})