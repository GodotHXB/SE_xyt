// app.js
App({
  score:[0,0],
  data_num1:[0,0,0,0,0,0,0,0,0],
  data_num2:[0,0,0,0,0,0,0,0,0],
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
  },
  globalData: {
    userInfo: null
  }
})
