
import Axios from 'axios'

import ajax from "./ajax"
import { HTTP, HOST, PORT, VERSION } from '../config'

const BASE_URL = `${HTTP}://${HOST}:${PORT}/${VERSION}`

// 根据 经纬度 获取地址
export const reqAddress = (geohash) => ajax(`${BASE_URL}/location/${geohash}`)

// 获取 店铺食品分类 的列表
export const reqFoodCategorys = () => ajax(BASE_URL + '/gategorys')

// 获取 商铺列表
export const reqShops = (geohash, keyword) => ajax(`${BASE_URL}/shops/?geohash=${geohash}&keyword=${keyword}`)



// 获取验证码
export const reqCaptcha = (username) => Axios.post(`${BASE_URL}/captcha/`, { 'phone': username })

// 用户名密码登录
export const reqPwdLogin = (username, password, code) => ajax(BASE_URL + '/login', { username, password, code }, 'POST') 

// 发送短信验证码
export const reqSendCode = (phone) => ajax(BASE_URL + '/send_code', {phone})

// 短信验证登录
export const reqSmsLogin = (phone, code) => ajax(BASE_URL + '/login_sms', { phone, code }, 'POST')

// 根据会话获取用户信息
export const reqUserInfo = () => ajax(BASE_URL + '/user')
