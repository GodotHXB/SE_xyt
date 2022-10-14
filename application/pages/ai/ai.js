// pages/ai/ai.js
Page({
  btn1:function(){
    wx.navigateTo({
      url: '../ai/easy/easy',
    })
  },
  btn_medium:function(){
    wx.navigateTo({
      url: '../ai/easy/easy'
    })
    // wx.navigateTo({
    //   url: '../ai/medium/medium'
    // })
  },
  btn_hard:function(){
    wx.navigateTo({
      url: '../ai/easy/easy'
    })
    // wx.navigateTo({
    //   url: '../ai/hard/hard'
    // })
  }
})