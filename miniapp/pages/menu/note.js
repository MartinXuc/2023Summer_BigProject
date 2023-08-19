Page({
    data: {
        note: '',
    },
    bindKeyInput: function (e) {
        this.setData({
            note: e.detail.value
        })
    },

    send_note: function () {
        var that = this;
        let pages = getCurrentPages();
        let prevPage = pages[pages.length - 2]; //上一个页面
        
        prevPage.setData({
            note: this.data.note,
            isnoteed: true,
        })
       
        wx.navigateBack({
            delta: 1
        })

    }
})