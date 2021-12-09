document.addEventListener('DOMContentLoaded', function() {  // open DOM of the page
const deleteItems = document.querySelectorAll('.js-delete-item'); // node list of all buttons 

Array.prototype.forEach.call(deleteItems, (item) => { // create array of delete buttons and assign function
    item.addEventListener('click', (e) => {  // call function when click
    console.log('click is worked!') 
    const id = +e.currentTarget.dataset.id;  // get id from data-id property
    const endpoint = e.currentTarget.dataset.endpoint; // get endpoint from data-enpoint property
    console.log('addres: ' +  endpoint + id) 
    
       httpDeleteAsync(endpoint, id) // call function which send request
       $('#DeleteDepModal'+id).modal('hide') // hide modal window
       e.currentTarget.closest('tr').remove(); // remove row from table with deleted data
              
    })
})

const editItems = document.querySelectorAll('.js-edit-item');

Array.prototype.forEach.call(editItems, (item) => { // create array of delete buttons and assign function
    item.addEventListener('submit', (e) => {  // call function when click
    console.log('click is worked!') 

    
       //httpPutAsync(endpoint, id) // call function which send request
 
          
       
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

function httpPutAsync(url, id, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 204)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("PUT", url+id, true); // true for asynchronous 
    xmlHttp.send(null);
}