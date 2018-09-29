import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

new Vue({
    el: '#app',
    render: V => V(App),
    router, // vue-router
    store // vuex
})
