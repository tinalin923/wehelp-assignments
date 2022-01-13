function init(){window.setTimeout(countdown,1000);}
function countdown(){alert("hello");}


const endpoint = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'; 
const request = new XMLHttpRequest();
request.open('GET', endpoint,true);     //xhr.open()，設定請求
request.send(null);                     //發送請求:單純請求資料(GET)，則xhr.send()可以是空值 -> xhr.send(null)
request.addEventListener('load', getRequest);    //因為發出請求時不一定可以即時拿到資料，所以必須監聽當請求得到回覆後，才往下執行程式碼，如果沒有這麼做的話會拿到空值。觸發事件的類型有很多，這邊則使用load事件，當目標資源加載完之後才觸發事件
function getRequest() {
  console.log(request);
  const charge = [];
  charge.push(...JSON.parse(request.responseText));   //當成功請求到資料時，會回傳一個DOMString，可以透過responseText屬性查看回應的內容，
                                                        //透過JSON.parse()的語法將資料(原為字串)轉成物件，如此一來才可以使用物件的操作技巧。
  createDomElement(charge);
}

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