/*
    直接更新 state 的多个方法对象
*/
import Vue from 'vue'
import {
    RECEIVE_ADDRESS,
    RECEIVE_CATEGORYS,
    RECEIVE_SHOPS,
    RECEIVE_TOKEN,
    RECEIVE_USERINFO,

    RECEIVE_GOODS,
    RECEIVE_INFO,
    RECEIVE_RATINGS,

    INCREMENT_FOOD_COUNT,
    DECREMENT_FOOD_COUNT,

    CLEAR_CART
} from './mutation-types'

export default {
    [RECEIVE_ADDRESS] (state, {address}) {
        state.address = address
    },
    
    [RECEIVE_CATEGORYS] (state, {categorys}) {
        state.categorys = categorys
    },
    
    [RECEIVE_SHOPS] (state, {shops}) {
        state.shops = shops
    },

    [RECEIVE_TOKEN] (state, {token}) {
        state.token = token
    },

    [RECEIVE_USERINFO] (state, {userInfo}) {
        state.userInfo = userInfo
    },

    [RECEIVE_INFO] (state, {info}) {
        state.info = info
    },

    [RECEIVE_RATINGS] (state, {ratings}) {
        state.ratings = ratings
    },

    [RECEIVE_GOODS] (state, {goods}) {
        state.goods = goods
    },

    [INCREMENT_FOOD_COUNT] (state, {food}) {
        if (!food.count) {
            Vue.set(food, 'count', 1) // 让新增的属性也有数据绑定

            state.cartFoods.push(food) // 加入购物车
        } else {
            food.count ++
        }
    },
    
    [DECREMENT_FOOD_COUNT] (state, {food}) {
        if (food.count) {
            food.count --
            if (food.count === 0) {
                state.cartFoods.splice(state.cartFoods.indexOf(food), 1) // 移除购物车
            }
        }
    },

    [CLEAR_CART] (state) {
        state.cartFoods.forEach(food => {
            food.count = 0
        })
        // 清空购物车
        state.cartFoods = []
    }
}
