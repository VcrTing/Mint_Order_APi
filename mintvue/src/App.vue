<template>
    <div id="app">
        <router-view/>
        <FooterGuide v-show="$route.meta.showFooter"/>
    </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import FooterGuide from './components/FooterGuide/FooterGuide.vue'

export default {
    async mounted () {
        this.getAddress() // this.$store.dispatch('getAddress')
        try {
            const token = window.localStorage.getItem('token')
            this.getUserInfo(token)
        } catch (e) {

        }
    },
    components: {
        FooterGuide
    },
    methods: {
        ...mapActions(['getAddress', 'getUserInfo'])
    }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
    #app
        width 100%
        height 100%
        background #f5f5f5
</style>
