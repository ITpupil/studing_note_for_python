console.log("content.js已加载");

// chrome.browserAction.onClicked.addListener(function(tab) {
// 	alert("chrome.browserAction.onClicked.addListener!已执行");

//    $('html *:not(script, style, noscript)').each(function() {
//    $(this).css("background", "pink");
   
// 	   });
   
//    });

// chrome.runtime.onMessage.addListener(function(request, sender, sendResponse)
// {
//    //  console.log(sender.tab ?"from a content script:" + sender.tab.url :"from the extension");
//    //  if(request.cmd == 'test') alert(request.value);
//     if(request.cmd == 'test') {console.log(request.value)};
//     sendResponse('我收到了你的消息！');
// });

// $('#start').click(start);
// $('#stop').click(stop);

// start()

var myVar=null;
var flag =0
function start(){
   if(myVar!=null){//判断计时器是否为空
      clearInterval(myVar);
      myVar=null;
   };
   myVar=setInterval(myTimer,1000);
}

function stop()
{ 
   clearInterval(myVar);
   myVar=null;
}

function myTimer()
{
   var d=new Date();
   var t=d.toLocaleTimeString();
   console.log(t);
   flag++;
   if(flag==3){stop()}
}

// if(typeof($('.footer'))=='object'){
//    console.log("object对象已早到，开始执行计时器");
//    start();
// }


console.log('content.js完成加载')


//计时器程序启动条件：1.页面hash；2.元素文本
function judge(hash,selecter,text){
   //hash:确定页面地址
   //selecter: 元素选择器
   //text:预知的元素文本
   if (window.location.hash==hash&&selecter==text) {
      return true
   } else {
      return false
   }
}


i =1
while(i<4){
   i++;
   console.log(i,"测试循环执行");
   start()
}