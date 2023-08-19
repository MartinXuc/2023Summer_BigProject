const app = getApp()

Page({
    data: {
        code: null,
        canIUse: wx.canIUse('button.open-type.getUserInfo')
    }, 

    login: function () {
        wx.login({
            success: function (res) {
                console.log(res.code)
                wx.request({
                    url: app.globalData.login,
                    method: 'POST',
                    data: {
                        code: res.code,
                        name: 'highvorz',
                        gender: 0,
                        avartarUrl: ''
                    },
                    header: {
                        "Content-Type": "application/x-www-form-urlencoded"
                    },
                    success: function (res) {
                        console.log(res)
                        if (res.data.code == 200)
                            console.log("登录成功")
                            app.globalData.status = true
                    },
                    fail: function(res){
                        console.log("request fail")
                        console.log(res)
                    }
                })
            }
        })
    },

    onLoad: function () {
        wx.login({
          success: (res) => {
            console.log(res.code)
          },
        })
    },
    bindGetUserInfo(e) {
        console.log(e.detail.userInfo)
    }
})