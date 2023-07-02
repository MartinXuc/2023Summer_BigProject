//获取应用实例
var app = getApp();
Page({
    data: {
        addressList: []
    },
    selectTap: function (e) {
        //从商品详情下单选择地址之后返回
        wx.navigateBack({});
    },
    addessSet: function (e) {
        wx.navigateTo({
            url: "/pages/my/addressSet"
        })
    },
    onShow: function () {
        var that = this;
        that.setData({
            addressList: [
                {
                    id:1,
                    name: "demo",
                    mobile: "12345678901",
                    detail: "上海市宝山区",
                    isDefault: 1
                },
                {
                    id: 2,
                    name: "你的名字",
                    mobile: "12345678901",
                    detail: "上海市浦东新区XX"
                }
            ]
        });
    }
});
