
import Axios from 'axios'

import {ajax, ajax_auth} from "./ajax"
import { HTTP, HOST, PORT, VERSION } from '../config'

const BASE_URL = `${HTTP}://${HOST}:${PORT}`
const VERSION_URL = `${HTTP}://${HOST}:${PORT}/${VERSION}`

// 根据 经纬度 获取地址
export const reqAddress = (geohash) => ajax(`${VERSION_URL}/location/${geohash}`)

// 获取 店铺食品分类 的列表
export const reqFoodCategorys = () => ajax(VERSION_URL + '/gategorys')

// 获取 商铺列表
export const reqShops = (geohash, keyword) => ajax(`${VERSION_URL}/shops/?geohash=${geohash}&keyword=${keyword}`)

// 获取验证码
export const reqCaptcha = (username) => Axios.post(`${VERSION_URL}/captcha/`, { 'username': username })

// 注册
export const reqRegister = (username, password, sms_code, captcha_code) => ajax(VERSION_URL + '/users/', { username, password, sms_code, captcha_code }, 'POST') 

// 登录
export const reqLogin = (username, password) => ajax(BASE_URL + '/login/', { username, password }, 'POST') 

// 根据会话获取用户信息
export const reqUserInfo = (the_token) => ajax_auth(`${VERSION_URL}/users/999`, the_token)

/**
 * mock 数据
 */

// 获取商家信息
export const reqShopInfo = () => ajax('/info')

// 获取商家评价数组
export const reqShopRatings = () => ajax('/ratings')

// 获取商家商品数组
export const reqShopGoods = () => ajax('/goods')
