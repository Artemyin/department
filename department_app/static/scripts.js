document.addEventListener('DOMContentLoaded', function() {
const deleteItems = document.querySelectorAll('.js-delete-item');


Array.prototype.forEach.call(deleteItems, (item) => {
    item.addEventListener('click', (e) => {
    console.log('click is worked!')
    const id = +e.currentTarget.dataset.id; // это твой айди на текущей кнопке 
    const endpoint = e.currentTarget.dataset.endpoint;
    console.log('addres: ' +  endpoint + id) 
    
        httpDeleteAsync(endpoint, id)
        e.currentTarget.closest('tr').remove();
    })
})

});


function httpDeleteAsync(url, id, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 204)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("DELETE", url+id, true); // true for asynchronous 
    xmlHttp.send(null);
}