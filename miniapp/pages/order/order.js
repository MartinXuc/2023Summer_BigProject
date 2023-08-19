const app = getApp();

Page({
    data: {
        icon: {
            return: '/images/icon-return-dark.png',
        },
        exist_order: true,
        tags: ['全部', '未完成', '已完成'],
        order_list: [],
        classify_list: [],
        selected_id: 0,
    },

    select_orderlist: function (e) {
        let id = e.target.dataset.id;
        this.setData({
            selected_id: id,
        })
    },


    onLoad: function () {
        this.getOrder();
    },

    return: function () {
        wx.navigateTo({
          url: '../home/home',
        })();
    },

    gotoMenu: function () {
        wx.navigateTo({
            url: '../menu/menu',
        })
    },

    dateData: function() { 
        return function(a, b) {
            var date1 = a['date'];
            var date2 = b['date'];
            var status1 = a['status'];
            var status2 = b['status'];

            if(status1 != status2)
                return status1 < status2;
            
            return Date.parse(date2) - Date.parse(date1);
            
        }
    },

    getOrder: function () {
        var that = this;
        wx.request({
            url: app.globalData.get_order_url,
            method: 'POST',
            header: {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": app.globalData.token,
            },
            success: function (res) {
                that.setData({
                    order_list: res.data.data.pay_order_list,
                })

                var new_classify_list = [
                    [],
                    [],
                    [],
                ];

                var list = that.data.order_list;


                for (var item in list) {
                    new_classify_list[0].push(list[item]);
                    switch (list[item].status) {
                        case -8:
                            new_classify_list[1].push(list[item])
                            break;
                        case 1:
                            new_classify_list[2].push(list[item])
                            break;
                    }
                }
                that.setData({
                    classify_list: new_classify_list,
                })
            }
        })



    },

    pay: function (e) {
        let item = e.target.dataset.id.order_sn;
        var that = this;
        wx.request({
            url: app.globalData.pay_url,
            method: 'POST',
            header: {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": app.globalData.token,
            },
            data: {
                order_sn: item,
            },
            success: function (res) {
                that.getOrder();
                console.log('pay success')
            }
        })
    }
})