//fetch為一非同步程式，在fetch處理問題時，電腦不會等fetch處理完才跑後續
    //是物件，是類字串
let listname=[];
let listpic=[];
function getData(){
    let src = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'; 
    fetch (src)
    .then(function(response){
        //console.log(response);  //response為一物件，代表伺服器的回應
        //return response.text(); //用字串的方式取回資料
        return response.json(); //將資料用json的格式詮釋成:物件和陣列的組合 
    })
    .then(function(data){
        let list=data.result.results;
        //console.log(list);   //list 為物件，且為類字串   "results":[{},{},{}]
        //console.log(list[0].stitle);       // 不是類字串,為字串
        //console.log(isArrayLike(list[0]["stitle"]));    // 不是類字串,為字串
        //console.log(list.length);
        list.forEach(function callback(place){
            let placename=place.stitle;
            listname.push(placename);
            return listname;

        });
        console.log(listname);
        // list.forEach(function callback(place){
        //     let end = place.file.toLowerCase().search('jpg');
        //     let placepic=place.file.slice(0,end+3);
        //     listpic.push(placepic);
        //     return listpic;
        
        // });
    })
    .then(function (input){ 
        console.log(input);
        console.log(listname)
        ;
        // for (let i=0;i<9;i++){
        // let place = document.getElementsByClassName('wrapper');
        // console.log(typeof(place));
        // let newP = document.createElement('div');
        // let newpic = document.createElement('img');
        // newP.appendChild(newpic);
        // newpic.src=listpic[i];
        // place.appendChild(newP);
        // let newN = document.createElement('div');
        // let newname = document.createTextNode(listname[i]);   
        // newN.appendChild(newname);
        // newP.className="odd";  
        // newN.className = "even";
        // place.appendChild(newN);}
    })
    }
//console.log(listname);
//console.log(listpic);
// function input(){
//     for (let i=0;i<9;i++){
//         let place = document.getElementsByClassName('wrapper');
//         console.log(typeof(place));
//         let newP = document.createElement('div');
//         let newpic = document.createElement('img');
//         newP.appendChild(newpic);
//         newpic.src=listpic[i];
//         place.appendChild(newP);
//         let newN = document.createElement('div');
//         let newname = document.createTextNode(listname[i]);   
//         newN.appendChild(newname);
//         newP.className="odd";  
//         newN.className = "even";
//         place.appendChild(newN);
//     }
// }
    

        // for(let i=0;i<list.length;i++){
        //     let placename=list[i].stitle;
        //     listname.push(placename);

        //     console.log(placename); //回傳的是字串，placename不是類字串
            
        // }    
        // let i = 0;
        // let place=list[i].stitle;
        // list.forEach(function(place,i){
        //     listname.push(place)
        //     console.log(i,place);
            
        // });

// })
    //console.log(typeof(listname));// 是物件，是類字串
    

