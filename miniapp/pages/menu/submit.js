const app = getApp()

Page({
    data: {
        check: {},
        seat_id: '未选',
        methodCard_style_unselected: "shopInfo-method-card",
        methodCard_style_selected: "shopInfo-method-card-selected",
        method: 'eat_in',
        hasNote: false,
        note: '',
    },

    onLoad: function(options){
        this.setData({
            check: JSON.parse(options.check),
            seat_id: app.globalData.seat_id,
        })
    },

    onShow: function(){
        if(this.hasNote){
            console.log(this.data.note)
        }
    },

    select_method: function(e){
        var res = e.currentTarget.dataset.id;
        if(res == "eat_in"){
            this.setData({
                methodCard_style_unselected: "shopInfo-method-card",
                methodCard_style_selected: "shopInfo-method-card-selected",
                method: 'eat_in',
            })
        }
        else{
            this.setData({
                methodCard_style_unselected: "shopInfo-method-card-selected",
                methodCard_style_selected: "shopInfo-method-card",
                method: 'eat_out',
            })
        }
    },

    return: function(){
        wx.navigateBack();
    },

    gotoNote: function(){
        wx.navigateTo({
          url: '../menu/note',
        })
    },

    gotoOrder: function(){
        wx.navigateTo({
          url: '../order/order',
        })
    },

    submit: function(){
        if(!app.globalData.login_status){
            wx.showModal({
                title: '提示',
                content: '用户未登录',
                success: function (res) {
                }
              })
            return;
        }
        this.setData({
            ['check.method']: this.data.method,
            ['check.seat_id']: this.data.seat_id,
        })

        var that = this;
        wx.request({
          url: app.globalData.send_order_url,
          method: 'POST',
          data:{
              goods: JSON.stringify(this.data.check),
              note: that.data.note,
          },
          header: {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": app.globalData.token,
          },
          success: function(res){
            wx.showModal({
                title: '提示',
                content: '订单已提交',
                success: function(res) {
                    that.gotoOrder()
                }
              })
          },
        })
    },

})