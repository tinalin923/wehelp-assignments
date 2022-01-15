let src = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'; 
fetch (src).then(function(response){
    //console.log(response);  //response為一物件，代表伺服器的回應
    //return response.text(); //用字串的方式取回資料
    return response.json(); //將資料用json的格式詮釋成:物件和陣列的組合 
}).then(function(re){
    console.log(re);

})
function getRequest() {
    let data = JSON.parse(request.responseText.toLowerCase());
    let list = data["result"]["results"];    
    let oldname = document.querySelectorAll(".even");
    let oldpic = document.querySelectorAll(".odd");
    for (let i=0;i<oldname.length;i++){
        let place = document.getElementById('place'+i);
        let newN = document.createElement('div');
        let newname = document.createTextNode(list[i]["stitle"]);   
        newN.appendChild(newname);  
        newN.className = "even";
        place.replaceChild(newN, oldname[i]);
    }
    for (let i=0;i<oldpic.length;i++){
        let place = document.getElementById('place'+i);
        let newP = document.createElement('div');
        let newpic = document.createElement('img');
        newP.appendChild(newpic);
        newP.className="odd";
        let web = list[i]["file"];
        let end = web.search('jpg'); 
        newpic.src = web.slice(0,end+3);
        place.replaceChild(newP, oldpic[i]);
    }
}
