/*
    通过mutation间接更新 state 的多个方法的对象
*/

import {
    RECEIVE_ADDRESS,
    RECEIVE_CATEGORYS,
    RECEIVE_SHOPS
} from './mutation-types'

import {
    reqAddress,
    reqFoodCategorys,
    reqShops
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
    } 
}
