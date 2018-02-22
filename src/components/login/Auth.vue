<template>
<div>
    <h1>Auth</h1>
    <div id='firebaseui-auth-container'></div>
</div>
</template>
<script>

import { config } from '../../helpers/firebaseConfig'
import firebase from 'firebase'
import firebaseui from 'firebaseui'

export default {
    data() {
        return {

        }
    },
    created() {
        var uiConfig = {
            signInSuccessUrl : '/Profile',
            signInOptions: [
                firebase.auth.GoogleAuthProvider.PROVIDER_ID,
                firebase.auth.EmailAuthProvider.PROVIDER_ID,
                firebase.auth.FacebookAuthProvider.PROVIDER_ID,
                firebase.auth.TwitterAuthProvider.PROVIDER_ID,
            ]
        }
        var ui = new firebaseui.auth.AuthUI(firebase.auth())
        ui.start('#firebaseui-auth-container',uiConfig)
    },
    destroyed() {

    },
    methods: {

    }
}
</script>