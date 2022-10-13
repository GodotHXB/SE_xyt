// pages/online/online.js
Page({
  data: {
    inputValue: ''
  },
  bindKeyInput: function (e) {
    this.setData({
      inputValue: e.detail.value
    })
  },
  btn:function(){
    if(this.data.inputValue==''){
      
    }
    else{
      wx.navigateTo({
        url: '../online/battle/battle'
      })
    }
  }
})