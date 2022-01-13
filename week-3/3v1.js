//練習 測驗
// function init(){window.setTimeout(countdown,1000);}
// function countdown(){alert("hello");}

//正式
const request = new XMLHttpRequest();   //要設定在全域空間，之後其他function才可使用此全域變數
function getData(){
    const endpoint = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'; 
    //const request = new XMLHttpRequest();  原本設定在這裡，但是getRequest()會用不到
    request.open('GET', endpoint);     //xhr.open()，設定請求
    request.send();                    //發送連線請求:單純請求資料(GET)，則xhr.send()可以是空值 -> xhr.send(null)
    request.addEventListener('load', getRequest);    //因為發出請求時不一定可以即時拿到資料，所以必須監聽當請求得到回覆後，才往下執行程式碼，如果沒有這麼做的話會拿到空值。
}                                                        //觸發事件的類型有很多，這邊則使用load事件，當目標資源加載完之後才觸發事件(getRequsest此函式)

function getRequest() {
    // //法一 (無法作用，也沒有用creatElement)
    // let place = document.getElementById("place");
    // let newpic = place.querySelectorAll("div")[0];
    // let newname = place.querySelectorAll("div")[1];
    // newpic.style
    // newname.innerHTML= "北投溫泉";}
    // //法二 (不符合使用)
    // let jschange =document.getElementById("place").querySelectorAll("div");
    // let i;
    // for (i=0;i<jschange.length;i++){
    //     jschange[i].style.backgroundColor="green";
    //     jschange[i].style.color = "white"
    // 
    let oldname = document.querySelectorAll(".even");
     //console.log(oldname); //為一個node list
    
   
    //第一組
    let place0 =document.getElementById('place0');
    let newDiv0 = document.createElement('div');     //在建立新的 div 元素節點 newDiv 後，這時候我們在瀏覽器上還看不到它，透過 appendChild()、insertBefore() 或 replaceChild()將新元素加入至指定的位置之後才會顯示
    // newDiv.id = "myNewDiv";  新建立的 newDiv 我們也可以同時對它指定屬性
    // newDiv.className = "box";
    let newName0 = document.createTextNode("我愛你");   //建立文字節點， ()內加入字串
    newDiv0.appendChild(newName0);  //透過 newDiv.appendChild 將 textNode 加入至 newDiv
    place0.replaceChild(newName0, oldname[0]);
    //第二組
    let place1 =document.getElementById('place1');
    let newDiv1 = document.createElement('div');    
    let newName1 = document.createTextNode("我愛你");   
    newDiv1.appendChild(newName1);
    place1.replaceChild(newName1, oldname[1]);
    //console.log(typeof(request.responseText));  //為一字串，必須透過JSON.parse轉為物件
    let data=JSON.parse(request.responseText);
    let list=data["result"]["results"];
    //console.log (typeof(list));


    }
  


    
    //document.write(request.responseText)    //當網頁已經讀取(onload)完成後才執行 document.write()，則裡面的內容(request.responseText)會完全覆蓋掉目前的網頁
  
//     let y=request.responseText.result;
//     console.log(y);
//     console.log(typeof(request.responseText));
// }
//     const charge = [];
//     charge.push(...JSON.parse(request.responseText));   //當成功請求到資料時，會回傳一個DOMString，可以透過responseText屬性查看回應的內容，
//                                                         //透過JSON.parse()的語法將資料(原為字串)轉成物件，如此一來才可以使用物件的操作技巧。
//     createDomElement(charge);


// function createDomElement(charge) {
//     const domElements = charge.map(place => {
//       return `
//       <li>
//         <p class="location">位置： ${ place.Location }</p>
//         <p class="address">地址：${ place.Address }</p>
//       </li>
//     `;
//     }).join("");
    
//     const chargeList = document.querySelector('.charge-list');
//     chargeList.innerHTML = domElements;
//   }