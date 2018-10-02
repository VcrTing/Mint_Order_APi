/*
    包含多个基于 state 的getter计算属性的对象
*/

export default {
    totalCount (state) {
        return state.cartFoods.reduce((preTotal, food) => preTotal + food.count, 0)
    },
    totalPrice (state) {
        return state.cartFoods.reduce((preTotal, food) => preTotal + food.count * food.price, 0)
    },
}
