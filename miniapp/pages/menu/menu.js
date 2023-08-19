const app = getApp()
const Decimal = require('../../utils/decimal');

Page({
    data: {
        toView: 'default',
        swipers: [],
        foodlist: {},
        icon: {
            'orderbar': '/images/icon-hamburg.png'
        },
        expense: 0,
        total: 0,
        order: {},
        kinds: 0,
        detail_status: false,
        height: 0,
        detail_style: "hiden-detail",
        whole_style: "whole-before",
        package: null,
        foods: {},
    },

    gotoSubmit: function () {
        let check = {
            order: this.data.order,
            expense: this.data.expense,
        }
        let checkStr = JSON.stringify(check)
        wx.navigateTo({
            url: '../menu/submit?check=' + checkStr,
        })
    },

    submit: function () {
        console.log(this.data.order);
        if (app.globalData.status != true) {
            wx.showModal({
                title: '未登录',
                content: '请先登录',
                success: function (res) {
                    if (res.confirm) {
                        console.log('用户点击确定')
                    } else {
                        console.log('用户点击取消')
                    }
                }
            })
        }
        wx.request({
            url: app.globalData.submit,
            method: 'POST',
            data: {
                Order: this.data.order
            },
            header: {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": app.globalData.token,
            },
        })
    },

    addPackage: function (item) {
        this.setData({
            package: item,
        })
    },

    requestSync: function (_url, _data, _method, _callback) {
        return new Promise(function () {
            wx.request({
                url: _url,
                data: _data,
                method: _method,
                success: function (res) {
                    resolve(res);
                },
                fail: function (res) {
                    reject(res);
                },
                complete: function (res) {
                    if (_callback) {
                        _callback(res);
                    }
                }
            })
        })
    },


    onLoad: function (options) {
        var that = this;

        // 请求食物列表
        wx.request({
            url: app.globalData.foodlist,
            method: 'GET',
            success: function (res) {
                that.request_list_success(res)
                // 
                if (options) {
                    let item = JSON.parse(options.package)
                    that.addPackage(item)
                    that.addFood(item.food_id)
                }
            },
            fail: function (res) {
                console.log(res);
            }
        })
        
        // 请求swipers

        wx.request({
            url: app.globalData.swipers,
            method: 'GET',
            success: function (res) {
                console.log(res)
                that.setData({
                    swipers: res.data.data.swipers,
                })
            }
        })


    },

    request_list_success: function (res) {
        let t = res.data.data;
        this.setData({
            foodlist: t,
        });
        let array = {}
        for (var key in t) {
            let foods = t[key].classfy_list;
            for (var index in foods) {
                let food = foods[index]
                array[food.id] = food
            }
        };
        this.setData({
            foods: array,
        })
    },



    scroll: function (e) {
        this.setData({
            toView: 'view' + e.currentTarget.dataset.smile,
        })
    },


    //#region  page navigator
    return: function () {
        wx.navigateBack();
    },

    gotoGuide: function () {
        wx.navigateTo({
            url: '../guide/guide',
        })
    },
    //#endregion

    //#region detail
    show_detail: function () {
        this.setData({
            detail_style: "show-detail",
            whole_style: "whole-after",
            detail_status: true,
            height: this.data.kinds * 100 + 150,
        })
    },

    hiden_detail: function () {
        this.setData({
            detail_style: "hiden-detail",
            whole_style: "whole-before",
            detail_status: false,
            height: 0,
        })
    },

    detail_button: function () {
        if (!this.data.detail_status) {
            this.show_detail();
        } else {
            this.hiden_detail();
        }
    },


    addFood: function (id) {
        let food = this.data.foods[id]
        if (!(id in this.data.order)) {
            this.setData({
                ['order.' + id]: food,
                ['order.' + id + '.number']: 1,
                kinds: this.data.kinds + 1,
            })
        } else {
            var cnt = this.data.order[id].number;
            this.setData({
                ['order.' + id + '.number']: cnt + 1,
            })
        }


        var discount = parseFloat(0)
        console.log(id)
        if (this.data.package && id == this.data.package.food_id) {
            discount = parseFloat(this.data.package.discount)
            console.log(discount)
        }

        

        var price = parseFloat(food.price)
        var exp = parseFloat(this.data.expense)

        exp = (price + exp - discount).toFixed(2)
        var count = parseFloat(food.price)
        count = (count * this.data.order[food.id].number).toFixed(2)

        this.setData({
            expense: exp,
            ['order.' + food.id + '.count']: count,
            total: this.data.total + 1
        })
    },

    minusFood: function (id) {
        var food = this.data.foods[id]
        console.log('---------------')
        console.log(food)

        var discount = parseFloat(0)
        if (this.data.package && id == this.data.package.food_id && this.data.order[id].number == 1) {
            discount = parseFloat(this.data.package.discount)
            console.log(discount)
        }

        var price = parseFloat(food.price)
        var exp = parseFloat(this.data.expense)
        exp = (exp - price + discount).toFixed(2)
        var count = parseFloat(food.price)
        count = (count * number).toFixed(2)

        var number = food.number;
        number = number - 1
        this.setData({
            ['order.' + food.id + '.number']: number,
            total: this.data.total - 1,
            expense: exp,
            ['order.' + food.id + '.count']: count,
        })

        // goods number
        if (number == 0) {
            let new_order = this.data.order;
            delete new_order[food.id];
            console.log(new_order)
            this.setData({
                order: new_order,
                kinds: this.data.kinds - 1,
            })
            if (this.data.total == 0) {
                this.hiden_detail()
            }
        }
    },

    add_button: function (e) {
        this.addFood(e.target.dataset.id);
    },

    minus_button: function (e) {
        this.minusFood(e.target.dataset.id);
    },

    clear: function (e) {
        this.setData({
            total: 0,
            expense: 0,
            order: {},
            kinds: 0,
        })
        this.hiden_detail()
    },
    //#endregion
})