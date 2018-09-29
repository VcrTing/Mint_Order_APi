<template>
    
  <section class="loginContainer">
    <div class="loginInner">
      <div class="login_header">
        <h2 class="login_logo">Mint外卖</h2>
        <div class="login_header_title">
          <a href="javascript:;" :class="{on: loginWay}" @click="loginWay=true">短信登录</a>
          <a href="javascript:;" :class="{on: !loginWay}" @click="loginWay=false">密码登录</a>
        </div>
      </div>
      <div class="login_content">
        <form @submit.prevent="login">
          <div :class="{on: loginWay}">
            <section class="login_message">
              <input type="tel" maxlength="11" placeholder="手机号" v-model="phone">
              <button class="get_verification" :disabled="!rightPhone"
                :class="{right_phone: rightPhone}" @click.prevent="get_code">
                {{ computeTime > 0 ? `已发送（${computeTime}s）` : '获取验证码' }}  
              </button>
            </section>
            <section class="login_verification">
              <input type="tel" maxlength="8" placeholder="验证码" v-model="vertify_code">
            </section>
            <section class="login_hint">
              温馨提示：未注册Mint外卖帐号的手机号，登录时将自动注册，且代表已同意
              <a href="javascript:;">《用户服务协议》</a>
            </section>
          </div>
          <div :class="{on: !loginWay}">
            <section>
              <section class="login_message">
                <input type="text" maxlength="11" placeholder="手机/邮箱/用户名" v-model="username">
              </section>
              <section class="login_verification">
                <input type="text" maxlength="8" placeholder="密码" v-if="showPwd" v-model="password">
                <input type="password" maxlength="8" placeholder="密码" v-else v-model="password">
                <div class="switch_button" :class="showPwd ? 'on' : 'off'" @click="showPwd=!showPwd">
                  <div class="switch_circle" :class="{right: showPwd}"></div>
                  <span class="switch_text">{{ showPwd ? 'abc' : '...' }}</span>
                </div>
              </section>
              <section class="login_message" v-show="showCaptcha">
                <input type="text" maxlength="11" placeholder="验证码" v-model="captcha_code">
                <img v-if="nowCaptcha" class="get_verification" :src="nowCaptcha" alt="captcha" ref="captcha" @click="get_captcha">
                <div v-else class="get_verification" @click="get_captcha"></div>
              </section>
            </section>
          </div>
          <button class="login_submit">登录</button>
        </form>
        <a href="javascript:;" class="about_us">关于我们</a>
      </div>
      <!--利用$router.back()返回上一级路由 -->
      <a href="javascript:" class="go_back" @click="$router.back()">
        <i class="iconfont icon-jiantou2"></i>
      </a>
    </div>
    <AlertTip :alertText='alertText' v-show="showAlert" @closeTip="closeTip"/>
  </section>
</template>

<script>
import Axios from 'axios'
import {MEDIA_DIR} from '../../config'

import AlertTip from '../../components/AlertTip/AlertTip.vue'
import {reqCaptcha} from '../../api'

export default {
  data () {
    return {
      loginWay: true, // true 为短信登录, false 为密码登录
      computeTime: 0, // 计时
      showPwd: false, // 是否显示明文密码
      showCaptcha: false, // 是否显示验证码框
      nowCaptcha: '', // 当前的验证码图片

      username: '', // 后台的用户名
      phone: '', // 电话
      password: '', // 密码
      vertify_code: '', // 短信验证码
      captcha_code: '', // 图片验证码

      alertText: '', // 提示文本
      showAlert: false, // 是否显示警告框
    }
  },
  watch: {
    password (new_val) {
      if (this.username.length >= 2){
        if (new_val.length >= 4) {
          this.showCaptcha = true
        } else {
          this.showCaptcha = false
        }
      }
    },
    username () {
      // 检测是否存在此用户
      if (this.password.length >= 4){

      }
    },
    showCaptcha (new_val) {
      if (new_val) {
        this.get_captcha ()
      }
    }
  },
  components: {
    AlertTip
  },
  computed: {
    rightPhone () {
      return /^1\d{10}$/.test(this.phone)
    }
  },
  methods: {
    // 获取图片验证码
    get_captcha () {
      reqCaptcha(this.username)
        .then( response => {
          const ret = response.data
          if (response.status === '201') {
            this.show_alert('服务器错误，请重试！')
          } else {
            this.nowCaptcha = MEDIA_DIR + ret.img_content
          }
        })
        .catch( error => {
          console.info(error)
        })
    },
    // 获取短信验证码
    get_code () {
      if (!this.computeTime) {
        // 启动倒计时
        this.computeTime = 30
        const interId = setInterval(() => {
          this.computeTime --
          if (this.computeTime <= 0) {
            // 停止计时
            clearInterval(interId)
          }
        }, 1000)
        // 向指定手机号发送验证码短信
      } 
    },
    show_alert (alertText) {
      this.showAlert = true
      this.alertText = alertText
    },
    // 前台表单验证
    login () {
      // 登录方式
      if (this.loginWay) { // 短信登录
        const {rightPhone, phone, vertify_code} = this
        if (!this.rightPhone) {
          this.show_alert('手机号不正确')
        } else if (!/^\d{4}$/.test(this.vertify_code)) {
          this.show_alert('手机验证码不正确')
        }
      } else { // 密码登录
        const {username, password, captcha_code} = this
        if (!this.username) {
          this.show_alert('必须指定用户名')
        } else if (!this.password) {
          this.show_alert('密码必须指定')
        } else if (!/^\w{4}$/.test(this.captcha_code)) {
          this.show_alert('验证码必须是 4 位')
        }
      }
    },
    closeTip () {
      this.showAlert = false
      this.alertText = ''
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../common/stylus/mixins.styl"
  .loginContainer
    width 100%
    height 100%
    background #fff
    .loginInner
      padding-top 60px
      width 80%
      margin 0 auto
      .login_header
        .login_logo
          font-size 40px
          font-weight bold
          color #02a774
          text-align center
        .login_header_title
          padding-top 40px
          text-align center
          >a
            color #333
            font-size 14px
            padding-bottom 4px
            &:first-child
              margin-right 40px
            &.on
              color #02a774
              font-weight 700
              border-bottom 2px solid #02a774
      .login_content
        >form
          >div
            display none
            &.on
              display block
            input
              width 100%
              height 100%
              padding-left 10px
              box-sizing border-box
              border 1px solid #ddd
              border-radius 4px
              outline 0
              font 400 14px Arial
              &:focus
                border 1px solid #02a774
            .login_message
              position relative
              margin-top 16px
              height 48px
              font-size 14px
              background #fff
              .get_verification
                position absolute
                top 50%
                right 10px
                transform translateY(-50%)
                border 0
                color #ccc
                font-size 14px
                background transparent
                &.right_phone
                  color black
            .login_verification
              position relative
              margin-top 16px
              height 48px
              font-size 14px
              background #fff
              .switch_button
                font-size 12px
                border 1px solid #ddd
                border-radius 8px
                transition background-color .3s,border-color .3s
                padding 0 6px
                width 30px
                height 16px
                line-height 16px
                color #fff
                position absolute
                top 50%
                right 10px
                transform translateY(-50%)
                &.off
                  background #fff
                  .switch_text
                    float right
                    color #ddd
                &.on
                  background #02a774
                >.switch_circle
                  //transform translateX(27px)
                  position absolute
                  top -1px
                  left -1px
                  width 16px
                  height 16px
                  border 1px solid #ddd
                  border-radius 50%
                  background #fff
                  box-shadow 0 2px 4px 0 rgba(0,0,0,.1)
                  transition transform .3s
                  &.right
                    transform translateX(26px)
            .login_hint
              margin-top 12px
              color #999
              font-size 14px
              line-height 20px
              >a
                color #02a774
          .login_submit
            display block
            width 100%
            height 42px
            margin-top 30px
            border-radius 4px
            background #4cd96f
            color #fff
            text-align center
            font-size 16px
            line-height 42px
            border 0
        .about_us
          display block
          font-size 12px
          margin-top 20px
          text-align center
          color #999
      .go_back
        position absolute
        top 5px
        left 5px
        width 30px
        height 30px
        >.iconfont
          font-size 20px
          color #999
</style>
