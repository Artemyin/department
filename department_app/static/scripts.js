document.addEventListener('DOMContentLoaded', function() {  // open DOM of the page
const deleteItems = document.querySelectorAll('.js-delete-item'); // node list of all buttons 

Array.prototype.forEach.call(deleteItems, (item) => { // create array of delete buttons and assign function
    item.addEventListener('click', (e) => {  // call function when click
    console.log('delete click is worked!') 
    const id = +e.currentTarget.dataset.id;  // get id from data-id property
    const endpoint = e.currentTarget.dataset.endpoint; // get endpoint from data-enpoint property
    console.log('addres: ' +  endpoint + id) 
    
       httpDeleteAsync(endpoint, id) // call function which send request
       $('#DeleteDepModal'+id).modal('hide') // hide modal window
       $('#EditDepModal'+id).modal('hide') // hide modal window
       e.currentTarget.closest('tr').remove(); // remove row from table with deleted data
              
    })
})
});


document.addEventListener('DOMContentLoaded', function() {
const editItems = document.querySelectorAll('.js-edit-item');

Array.prototype.forEach.call(editItems, (item) => { // create array of delete buttons and assign function
    item.addEventListener('click', (e) => {  // call function when click
    e.preventDefault();
    const id = +e.currentTarget.dataset.id;  // get id from data-id property
    const endpoint = e.currentTarget.dataset.endpoint; // get endpoint from data-enpoint property
    const form = document.querySelector('#edit')
    const name = form.elements['name'].value
    
    console.log('edit submit click is worked!') 
    console.log(name, endpoint, id)
    const data = {"name": name}
    const jsondata = JSON.stringify(data)

    console.log(jsondata)
    httpPutAsync(endpoint, id, jsondata)
    $('#EditDepModal'+id).modal('hide') 
    document.location.reload(true)


    })
})

});


document.addEventListener('DOMContentLoaded', function() {
    const addItems = document.querySelector('.js-add-item');
    
    // create array of delete buttons and assign function
        addItems.addEventListener('onclick', (e) => {  // call function when click
        
        
        // const endpoint = e.currentTarget.dataset.endpoint; // get endpoint from data-enpoint property
        const form = document.querySelector('#add')
        const name = form.elements['name'].value
        const endpoint = form.elements['endpoint'].value
        
        console.log('edit submit click is worked!') 
        console.log(name, endpoint)
        const data = {"name": name}
        const jsondata = JSON.stringify(data)
    
        console.log(jsondata)
        httpPostAsync(endpoint, jsondata)
        $('#AddDepModal').modal('hide') 
        document.location.reload(true)
        e.preventDefault();
    
        })});
    

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


function httpPutAsync(url, id, data)
{
    var xmlHttp = new XMLHttpRequest();
    
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 204);
    }

    xmlHttp.open("PUT", url+id, true); // true for asynchronous 
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(data);
}


function httpPostAsync(url, data)
{
    var xmlHttp = new XMLHttpRequest();
    
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 204);
    }

    xmlHttp.open("POST", url, true); // true for asynchronous 
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(data);
}

