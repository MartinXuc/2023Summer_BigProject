const app = getApp();

Page({
    data:{
        barcode: '',
        qrcode: '',
    },

    
    return: function(){
        wx.navigateBack();
    },

    onLoad: function(){
        this.getBarcode();
        this.getQRcode();
    },

    getBarcode: function(){
        var that = this;
        console.log(app.globalData.barcode)
        wx.request({
          url: app.globalData.barcode,
          responseType: "arraybuffer",
          success(res){
            let path ="data:image/png;base64," + wx.arrayBufferToBase64(res.data)
            that.setData({
              barcode : path, 
            })
          }
        })
    },

    getQRcode: function(){
        var that = this;
        wx.request({
            url: app.globalData.qrcode,
            responseType: "arraybuffer",
            success(res){
              let path ="data:image/png;base64," + wx.arrayBufferToBase64(res.data)
              that.setData({
                qrcode : path, 
              })
            }
          })
    },

})