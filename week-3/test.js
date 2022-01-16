let url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';
function get(url) {
    console.log('Making fetch() request to: ' + url);
  
    let promise = new Promise((resolve, reject) => {
      fetch(url).then(response => {
        if (response.ok) {
          const contentType = response.headers.get('Content-Type') || '';
  
          if (contentType.includes('application/json')) {
            response.json().then(obj => {
              resolve(obj);
            }, error => {
              reject(new ResponseError('Invalid JSON: ' + error.message));
            });
          } else if (contentType.includes('text/html')) {
            response.text().then(html => {
              resolve({
                page_type: 'generic',
                html: html
              });
            }, error => {
              reject(new ResponseError('HTML error: ' + error.message));
            });
          } else {
            reject(new ResponseError('Invalid content type: ' + contentType));
          }
        } else {
          if (response.status == 404) {
            reject(new NotFoundError('Page not found: ' + url));
          } else {
            reject(new HttpError('HTTP error: ' + response.status));
          }
        }
      }, error => {
        reject(new NetworkError(error.message));
      });
    });
    return promise;
  }
async function load(){
    let list= await get(url);
    let data=list.result.results;
    //console.log(data);
   
    for(let i=0;i<8;i++){
        let intro = document.getElementById('wrapper');
        let place= document.createElement('div');
        intro.appendChild(place);
        let newP = document.createElement('div');
        let newpic = document.createElement('img');
        newP.appendChild(newpic);
        let web = data[i].file.toLowerCase();
        let end = web.search('jpg');
        newpic.src=web.slice(0,end+3);
        newP.className="odd";
        place.appendChild(newP);
        let listname = data[i].stitle;
        let newN = document.createElement('div');
        let newname = document.createTextNode(listname);   
        newN.appendChild(newname);
        newN.className = "even";
        place.appendChild(newN);
        
    }
}
async function load2(){
    let list= await get(url);
    let data=list.result.results;
    for(let i=8;i<16;i++){
        let intro = document.getElementById('wrapper');
        let place= document.createElement('div');
        intro.appendChild(place);
        let newP = document.createElement('div');
        let newpic = document.createElement('img');
        newP.appendChild(newpic);
        let web = data[i].file.toLowerCase();
        let end = web.search('jpg');
        newpic.src=web.slice(0,end+3);
        newP.className="odd";
        place.appendChild(newP);
        let listname = data[i].stitle;
        let newN = document.createElement('div');
        let newname = document.createTextNode(listname);   
        newN.appendChild(newname);
        newN.className = "even";
        place.appendChild(newN);
        
    }
}