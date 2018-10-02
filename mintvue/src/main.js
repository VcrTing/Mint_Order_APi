import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import {Button} from 'mint-ui'
import 'mint-ui/lib/button/style.css'

import './mock/mockServer'

Vue.component(Button.name, Button)

new Vue({
    el: '#app',
    render: V => V(App),
    router, // vue-router
    store // vuex
})
