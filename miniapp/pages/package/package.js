const app = getApp();

Page({
    data: {
        title: '我的卡包',
        package: {},
    },

    onLoad: function () {
        this.get_package();
    },

    return: function () {
        wx.navigateBack();
    },

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
              url: '../menu/menu?package=' + packageStr,
            })
        }
    }
})