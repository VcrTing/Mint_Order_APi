/*
    通过mutation间接更新 state 的多个方法的对象
*/

import {
    RECEIVE_ADDRESS,
    RECEIVE_CATEGORYS,
    RECEIVE_SHOPS,
    RECEIVE_TOKEN,
    RECEIVE_USERINFO,

    RECEIVE_GOODS,
    RECEIVE_RATINGS,
    RECEIVE_INFO,

    INCREMENT_FOOD_COUNT,
    DECREMENT_FOOD_COUNT,

    CLEAR_CART
} from './mutation-types'

import {
    reqAddress,
    reqFoodCategorys,
    reqShops,
    reqUserInfo,

    reqShopInfo,
    reqShopRatings,
    reqShopGoods
} from '../api'

import {REST} from '../config'

export default {
    // 异步获取

    async getAddress ({commit, state}) {
        // 发送请求
        const geohash = state.latitude + ',' + state.longitude
        const result = await reqAddress(geohash)

        // 提交一个mutation
        if (result.code === REST['CODE_SUCCESS']) {
            const address = result.data
            commit(RECEIVE_ADDRESS, {address})
        }
    },

    async getCategorys ({commit}) {
        // 发送请求
        // const geohash = state.latitude + ',' + state.longitude
        const categorys = await reqFoodCategorys()

        // 提交一个mutation
        commit(RECEIVE_CATEGORYS, {categorys})
    },
    
    async getShops ({commit, state}) {
        // 发送请求
        const geohash = state.latitude + ',' + state.longitude
        const shops = await reqShops(geohash, '')

        // 提交一个mutation
        commit(RECEIVE_SHOPS, {shops})
    },
    
    recordToken ({commit, state}, token) {
        // 保存 token
        window.localStorage.setItem('token', token)
        commit(RECEIVE_TOKEN, {token})
    }, 

    async getUserInfo ({commit, state}, token) {
        // 发送请求
        const userInfo = await reqUserInfo(token)

        // 提交一个mutation
        commit(RECEIVE_USERINFO, {userInfo})
    },

    // 异步获取商家信息
    async getShopInfo ({commit}) {
        const result = await reqShopInfo()
        if (result.code === 0) {
        const info = result.data
        commit(RECEIVE_INFO, {info})
        }
    },

    // 异步获取商家评价列表
    async getShopRatings ({commit}, callback) {
        const result = await reqShopRatings()
        if (result.code === 0) {
        const ratings = result.data
        commit(RECEIVE_RATINGS, {ratings})
        // 数据更新了, 通知一下组件
        callback && callback()
        }
    },

    // 异步获取商家商品列表
    async getShopGoods ({commit}, callback) {
        const result = await reqShopGoods()
        if (result.code === 0) {
        const goods = result.data
        commit(RECEIVE_GOODS, {goods})
        // 数据更新了, 通知一下组件
        callback && callback()
        }
    },

    // 更新 food 中的 count 值
    updateFoodCount ({commit}, {isAdd, food}) {
        if (isAdd) {
            commit(INCREMENT_FOOD_COUNT, {food})
        } else {
            commit(DECREMENT_FOOD_COUNT, {food})
        }
    },

    // 清空购物车
    clearCart ({commit}) {
        commit(CLEAR_CART)
    }
}
