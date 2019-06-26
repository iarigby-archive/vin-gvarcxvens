console.log('hi')
base_href = window.document.location.origin
function Get(yourUrl){
    const Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET",yourUrl,false);
    Httpreq.send(null);
    return Httpreq.responseText;
}

function getListing(imageUrl, text) {
    const li = document.createElement('div')
    const image = document.createElement('img')
    image.src=imageUrl
    li.appendChild(image)
    li.appendChild(document.createTextNode(text))
    return li
}

function main() {
    const list = JSON.parse(Get('data/images/'))
    const text = 'data/images/'
    console.log(list)
    document.getElementById('list').appendChild(getListing(url, text)))
}
main()
