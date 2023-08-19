const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return `${[year, month, day].map(formatNumber).join('/')} ${[hour, minute, second].map(formatNumber).join(':')}`
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : `0${n}`
}

const login = {
    function () {
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
                    },
                })
            }
        })
    }
}

module.exports = {
  formatTime,
  login,
  
}
