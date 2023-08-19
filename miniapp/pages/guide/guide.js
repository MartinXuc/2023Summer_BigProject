const app = getApp();
const logs = [];

Page({
    data: {
        // 0 represents robot; 1 represents user;
        chat_log: [],
        avatar: ['/images/icon-robot.png', app.globalData.default_avatar],
        style: ['left-chat', 'right-chat'],
        block_style: ['default-robot-background', 'default-user-background'],
        question: null,
        empty: '',
    },

    

    bindKeyInput: function (e) {
        this.setData({
            question: e.detail.value,
        })
    },

    add_question(question){
        var log = {
            id: 1,
            text: question,
        }
        logs.push(log)
        this.setData({
            chat_log: logs,
        })

    },

    add_answer: function(answer){
        var log = {
            id: 0,
            text: answer,
        }
        logs.push(log);
        this.setData({
            chat_log: logs,
        })
    },


    sendButton: function () {
        var that = this;
        this.setData({
            empty: '',
        })

        this.add_question(this.data.question);
        // 
        wx.request({
            url: app.globalData.send_chat_with_guide,
            method: 'POST',
            data: {
                msg: this.data.question,
            },
            header: {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": app.globalData.token,
            },
            success: function (res) {
                console.log("你的问题是:\n" + res.data.question + '\n' + "我的回答是:\n" + res.data.answer);
                var answer = res.data.answer;
                that.add_answer(answer);
            }
        })
    },

    setChat: function () {
        let log = {
            id: 1,
            text: 'user'
        };
        logs.push(log);
        log = {
            id: 0,
            text: 'robot'
        };
        logs.push(log);
        this.setData({
            chat_log: logs
        })

    },

    onLoad: function () {
    },

    return: function () {
        wx.navigateBack();
    },


})