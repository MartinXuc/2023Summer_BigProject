const app = getApp()

Page({
    data: {
        login_status: app.globalData.login_status,
        default_avatar: app.globalData.default_avatar,
        userinfo: {},
        shop: {
            seat_id: '扫码点餐',
            address: '聚丰园路165号',
            time: '营业时间: 06:00-23:00',
        },
        icon: {
            icon_package: '/images/icon-package.png',
            icon_order: '/images/icon-order.png',
            icon_QRcode: '/images/icon-QRcode.png',
            mycard_package: '/images/icon-mycard-package.png',
            icon_drink: '/images/icon-drink.png',
            icon_tableware: '/images/icon-tableware.png',
        },
        discount: [

        ],
        resource: {},
        package: {},

        recommand: [{},
            {}
        ]

    },

    scan: function () {
        var that = this;
        wx.scanCode({
            onlyFromCamera: true,
            success(res) {
                var seat_id = JSON.parse(res.result).seat_id;
                that.setData({
                    'shop.seat_id': seat_id,
                })
                app.globalData.seat_id = seat_id;
            }
        })
    },

   

    loadres: function () {
        var that = this;

        wx.request({
            url: app.globalData.home_res,
            success: function (res) {
                that.setData({
                    resource: res.data.data.resource
                })
                console.log(res.data.data.resource)
            },
            fail: function (res) {
                console.log(app.globalData.home_res);
                console.log("request home_res failed");
            }
        })

    },

    getDiscount: function () {
        var that = this;
        wx.request({
            url: app.globalData.home_discount,

            success: function (res) {
                that.setData({
                    discount: res.data.data
                })
            },
        })
    },

    getLogin: function () {
        var that = this;
        wx.login({
            success: function (res) {
                console.log(res.code)
                // wx.request({
                //     url: app.globalData.login,
                //     method: 'POST',
                //     data: {
                //         code: res.code,
                //         name: 'highvorz',
                //         gender: 0,
                //         avatarUrl: ''
                //     },
                //     header: {
                //         "Content-Type": "application/x-www-form-urlencoded"
                //     },
                //     success: function (res) {
                //         console.log(res)
                //         if (res.data.code == 200)
                //             console.log("登录成功")
                //         app.globalData.login_status = true
                //         app.globalData.token = res.data.data.token
                //         console.log(app.globalData.token)
                //         that.setData({
                //                 login_status: app.globalData.login_status,
                //             }),
                //             // that.onLoad();
                //         that.after_login();
                //             console.log(that.data.login_status)
                //     },
                //     fail: function (res) {
                //         console.log("request fail")
                //         console.log(res)
                //     }
                // })
            }
        })
    },

    async getUserInfo() {
        const res = await wx.getUserProfile({
            desc: '用于完善会员资料',
        });
        console.log(res);
        app.globalData.avatar = res.userInfo.avatarUrl;
        app.globalData.username = res.userInfo.nickName;
        this.setData({
            userinfo: res.userInfo,
        })
        app.globalData.userinfo = res.userInfo;
        this.getLogin();
    },

    // 登录事件
    login: function () {
        this.getUserInfo();
    },

    after_login(){
        this.get_package();
    },

    getUserProfile() {
        wx.getUserProfile({
            desc: '用于完善会员资料',
            success: (res) => {
                console.log("获取用户信息成功", res)
                let user = res.userInfo;
                app.globalData.userInfo = res.userInfo;
                wx.setStorageSync('user', user)
                this.setData({
                    isShowUserName: true,
                    userInfo: user,
                    avatar: res.userInfo.avatarUrl,
                });
                this.assignPicChoosed();
            },
            fail: res => {
                console.log("获取用户信息失败", res)
            }
        })
    },
    toUser: function () {
        wx.navigateTo({
            url: '../user/user',
        })
    },

    toPackage: function () {
        wx.navigateTo({
            url: '../package/package',
        })
    },

    toOrder: function () {
        wx.navigateTo({
            url: '../order/order',
        })
    },

    toVipcode: function () {
        wx.navigateTo({
            url: '../vipcode/vipcode',
        })
    },

    toMenu: function () {
        wx.navigateTo({
            url: '../menu/menu',
        })
    },

    onLoad(options) {
        this.loadres();
        this.getDiscount();
    },

    onShow() {
        this.setData({
            login_status: app.globalData.login_status
        })
        if (app.globalData.login_status) {
            this.setData({
                userinfo: app.globalData.userinfo,
            })
        }
    },

    onHide() {

    },

    // package
    get_package: function () {
        var that = this;
        wx.request({
            url: app.globalData.get_package_url,
            method: 'POST',
            header: {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": app.globalData.token,
            },
            success: function (res) {
                that.setData({
                    package: res.data.data,
                }),
                that.process_date();
            }
        })

        
    },

    formatDate: function(date){
        var year = date.getFullYear();
        var month = date.getMonth() + 1;
        var day = date.getDate();
        return year + '.' + month + '.' + day;
    },

    process_date: function () {
        var list = this.data.package;
        for (var key in list) {
            var item = list[key];
            var validity = item.validity;
            // 
            var start_date = new Date(item.start_date);
            var start_date_str = this.formatDate(start_date);
            
            //
            var ended_date = start_date.setDate(start_date.getDate() + validity);
            var end_date = start_date;
            var end_date_str = this.formatDate(end_date);
            

            
            var current_date = Date.now(); 
            if(current_date > ended_date){
                list[key]['status'] = false
            }
            else{
                list[key]['status'] = true
            }
            
            
            list[key]['start_date_str'] = start_date_str;
            list[key]['end_date_str'] = end_date_str;

            console.log(list[key])
        }

        this.setData({
            package: list,
        })
    },

    usePackage: function(e){
        var item = this.data.package[e.target.dataset.id];
        if(item.status){
            let packageStr = JSON.stringify(item)
            wx.navigateTo({
              url: '../menu/menu?package' + packageStr,
            })
        }
    }

})