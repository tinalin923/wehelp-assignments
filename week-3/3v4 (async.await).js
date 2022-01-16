//fetch為一非同步程式，在fetch處理問題時，電腦不會等fetch處理完才跑後續
    //是物件，是類字串
function getData(){
let promise = new Promise ((resolve,reject)=>{
    let src = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'; 
    fetch (src)
    .then((response)=>{response.json().then(obj => {
        resolve(obj);
      })
    });return promise;
})}
   
async function load(){
    let list= await getData();
    console.log(list);}
    // let place = document.getElementsByClassName('wrapper');
    // for(let i=0;i<8;i++){
    //     let listname = list[i].stitle;
    //     let newN = document.createElement('div');
    //     let newname = document.createTextNode(listname);   
    //     newN.appendChild(newname);
    //     newN.className = "even";
    //     place.appendChild(newN);}
        
    // let end = list.file.toLowerCase().search('jpg');
    // let placepic=list.file.slice(0,end+3);
    // let 
    
        
        
        // listpic.push(placepic);
        // callback (listpic);


    // for (let i=0;i<9;i++){
    // let place = document.getElementsByClassName('wrapper');
    // let newP = document.createElement('div');
    // let newpic = document.createElement('img');
    // newP.appendChild(newpic);
    // newpic.src=listpic[i];
    // place.appendChild(newP);
    // newP.className="odd"; 
    // let newN = document.createElement('div');
    // let newname = document.createTextNode(listname[i]);   
    // newN.appendChild(newname);
    // newP.className="odd";  
    // newN.className = "even";
    // place.appendChild(newN);}

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