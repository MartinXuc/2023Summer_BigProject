App({

    initial: function(){

        // domain
        this.globalData.current_version = this.globalData.local_version;
        this.globalData.domain = this.globalData.current_version.domain;
        // api
        this.globalData.api = this.globalData.domain + '/' + this.globalData.api;
        this.globalData.home_discount = this.globalData.api + '/' + this.globalData.home_discount;
        this.globalData.swipers = this.globalData.api + '/' + this.globalData.swipers;
        this.globalData.home_res = this.globalData.api + '/' + this.globalData.home_res;
        this.globalData.foodlist = this.globalData.api + '/' + this.globalData.foodlist;
        this.globalData.login = this.globalData.api + '/' + this.globalData.login;
        this.globalData.submit = this.globalData.api + '/' + this.globalData.submit;
        this.globalData.qrcode = this.globalData.api + '/' + this.globalData.qrcode;
        this.globalData.barcode = this.globalData.api + '/' + this.globalData.barcode;
        this.globalData.send_order_url = this.globalData.api + '/' + this.globalData.send_order_url;
        this.globalData.get_order_url = this.globalData.api + '/' + this.globalData.get_order_url;
        this.globalData.pay_url = this.globalData.api + '/' + this.globalData.pay_url;
        this.globalData.get_package_url = this.globalData.api + '/' + this.globalData.get_package_url;
        this.globalData.send_chat_with_guide = this.globalData.api + '/' + this.globalData.send_chat_with_guide;
        // 
        this.globalData.resource = this.globalData.domain + '/' + this.globalData.resource;
    },

    onLaunch() {
        this.initial()
    },

    globalData: {

        // version
        current_version : {
            
        },
        
        server_version : {
            'domain': 'http://highvorz.website',
        },

        local_version : {
            'domain': 'http://192.168.5.246/:80',
        },

        // page data
        userinfo: {},

        // variable
        default_avatar: '/images/default_avatar.jpg',
        avatar: null,
        username: null,
        phone: null,
        code: null,
        login_status: false,
        userInfo: null,
        version: "1.0",
        token: null,
        seat_id: "未选",

        // request
        submit: 'order/create',
        home_discount: 'home/package',
        swipers: "menu/swipers",
        home_res: "home/resource",
        
        domain: '',
        api: "api",
        resource: "static/upload",
        foodlist: "food/index",
        login: "member/login",
        barcode: "vip/barcode",
        qrcode: "vip/qrcode",
        send_order_url: "order/create",
        get_order_url: "my/order",
        pay_url: "order/pay",
        get_package_url: "package",
        send_chat_with_guide: "guide",
    }

    
})