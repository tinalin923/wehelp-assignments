const request = new XMLHttpRequest();  
function getData(){
    const endpoint = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'; 
    
    request.open('GET', endpoint);     
    request.send();                    
    request.addEventListener('load', getRequest);

function getRequest() {
    
    let data=JSON.parse(request.responseText.toLowerCase());
    let list=data["result"]["results"];
    let web =list[0]["file"];
    let end= web.search('jpg');        
    console.log(web.slice(0,end+3));   


    let oldname = document.querySelectorAll(".even");
    let oldpic=document.querySelectorAll(".odd");
    
    
    //第一組
    //地名
    let place0 =document.getElementById('place0');
    let newN0 = document.createElement('div');   
    
    let newname0 = document.createTextNode(list[0]["stitle"]);   
    newN0.appendChild(newname0);  
    newN0.className = "even";
    place0.replaceChild(newN0, oldname[0]);
    //照片
    let newP0 = document.createElement("div");
    let newpic0 =document.createElement("img");
    newP0.appendChild(newpic0);
    newP0.className="odd";
    newpic0.src=web.slice(0,end+3);
    place0.replaceChild(newP0, oldpic[0]);
    
    
    //第二組
    let place1 =document.getElementById('place1');
    let newDiv1 = document.createElement('div');    
    let newName1 = document.createTextNode(list[1]["stitle"]);   
    newDiv1.appendChild(newName1);
    place1.replaceChild(newName1, oldname[1]);


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
    
    // const chargeList = document.querySelector('.charge-list');
    // chargeList.innerHTML = domElements;}
