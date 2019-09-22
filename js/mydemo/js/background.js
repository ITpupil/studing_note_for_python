console.log("background.js已加载")
 

function bg_test(){
    console.log("bg_test working");
};


//chrome.tabs.query报错 Uncaught TypeError: Cannot read property 'query' of undefined
// function sendMessageToContentScript(message, callback)
// {
//     chrome.tabs.query({active: true, currentWindow: true}, function(tabs)
//     {
//         chrome.tabs.sendMessage(tabs[0].id, message, function(response)
//         {
//             if(callback) callback(response);
//         });
//     });
// }


// sendMessageToContentScript({cmd:'test', value:'你好，我是background！'}, function(response)
// {
//     console.log('来自content的回复：'+response);
// });

