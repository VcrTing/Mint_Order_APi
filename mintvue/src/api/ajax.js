import axios from 'axios'

export default function ajax (url, data={}, type='GET') {
                        // 高阶函数: 接收函数的函数
    return new Promise((resolve, reject) => {
        let promise
        if (type === 'GET') {
            let data_str = ''
            Object.keys(data).forEach(key => {
                data_str += key + '=' + data[key] + '&'
            })
            if (data_str !== '') {
                data_str = data_str.substring(0, data_str.lastIndexOf('&'))
                url = url + '?' + data_str
            }
            promise = axios.get(url)
        }
        else {
            promise = axios.post(url, data)
        }

        promise.
            then( response => {
                resolve(response.data)
            }).
            catch( error => {
                reject(error)
            })
    })
}
