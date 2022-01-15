document.addEventListener('DOMContentLoaded', function() {  // open DOM of the page
const deleteItems = document.querySelectorAll('.js-delete-item'); // node list of all buttons 

Array.prototype.forEach.call(deleteItems, (item) => { // create array of delete buttons and assign function
    item.addEventListener('click', (e) => {  // call function when click
    console.log('delete click is worked!') 
    var id = +e.currentTarget.dataset.id;  // get id from data-id property
    const endpoint = e.currentTarget.dataset.endpoint; // get endpoint from data-enpoint property
    var orphan = document.getElementById('del-dep'+id);
    if (endpoint == '/departments/'){
    if (orphan.checked) {
		id = id + '?orphan=1';
	}
	else {
		id = id + '?orphan=0';
	}
    }
    console.log('addres: ' +  endpoint + id) 
    console.log(orphan) 
    
       httpDeleteAsync(endpoint, id) // call function which send request
    //    console.log(document.querySelector('#DeleteDepModal'+id))
          
       e.currentTarget.closest('tr').remove(); // remove row from table with deleted data
              
    })
})
});




document.addEventListener('DOMContentLoaded', function() {
const editItems = document.querySelectorAll('.js-edit-item');

Array.prototype.forEach.call(editItems, (item) => { // create array of delete buttons and assign function
    item.addEventListener('click', (e) => {  // call function when click
    // e.preventDefault();
    const id = +e.currentTarget.dataset.id;  // get id from data-id property
    const endpoint = e.currentTarget.dataset.endpoint; // get endpoint from data-enpoint property
    const form = document.querySelector('#edit'+id)
    console.log("this is form from modal" + form)
    console.log(form)

    if (endpoint == "/departments/") {
        const name = form.elements['name'].value
        var data = {"name": name}
        console.log("data inside if" + data)
        console.log(data)
    } else {
        const name = form.elements['name'].value  
        const birthdate = form.elements['birthdate'].value
        const salary = form.elements['salary'].value
        var department = form.elements['department'].value

        if (department == '') {
            department = null
        }
        var data = {
            "name": name,
            "birthdate": birthdate,
            "salary": salary,
            "department": department,
            }
        console.log("data inside else" + data)
        console.log(data)
    }
    console.log('edit submit click is worked!') 
    
    const jsondata = JSON.stringify(data)

    console.log("This is json")
    console.log(jsondata)
    httpPutAsync(endpoint, id, jsondata)
    // $('#EditDepModal'+id).modal('hide') 
    document.location.reload(true)


    })
})

});





document.addEventListener('DOMContentLoaded', function() {
    const AddDepItems = document.querySelector('#AddDepButton');       
    
    AddDepItems.addEventListener('click', (e) => {  // call function when click
        console.log("click is ok")
        const form = document.querySelector('#AddDep')
        const name = form.elements['name'].value  
        const endpoint = form.elements['endpoint'].value    

        const data = {"name": name}
        const jsondata = JSON.stringify(data)

        httpPostAsync(endpoint, jsondata)
        document.location.reload(true)
        e.preventDefault();
    
        });
    });
    
document.addEventListener('DOMContentLoaded', function() {
        
    const AddEmpItems = document.querySelector('#AddEmpButton');

    AddEmpItems.addEventListener('click', (e) => { 
        console.log("click is ok")
        const form = document.querySelector('#AddEmp')
            const name = form.elements['name'].value  
            const birthdate = form.elements['birthdate'].value
            const salary = form.elements['salary'].value
            var department = form.elements['department'].value

            if (department == '') {
                department = null
            }
            const endpoint = form.elements['endpoint'].value  
    
        const data = {
            "name": name,
            "birthdate": birthdate,
            "salary": salary,
            "department": department,
            }
        console.log(data)    
        const jsondata = JSON.stringify(data)
        console.log(jsondata)    
        httpPostAsync(endpoint, jsondata)
        // document.location.reload(true)
        e.preventDefault();     
        
        
        });
    });


function httpDeleteAsync(url, id)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 204);
    }
    xmlHttp.open("DELETE", '/api/v1'+url+id, true); // true for asynchronous 
    xmlHttp.send(null);
}


function httpPutAsync(url, id, data, callback)
{
    var xmlHttp = new XMLHttpRequest();
    
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 ){
            rspns = xmlHttp.response;
            console.log(rspns)
            callback(rspns)
        };
    }

    xmlHttp.open("PUT", '/api/v1'+url+id, true); // true for asynchronous 
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(data);
}


function httpPostAsync(url, data)
{
    var xmlHttp = new XMLHttpRequest();
    
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4){
            rspns = xmlHttp.response;
            console.log(rspns)
        };
    }

    xmlHttp.open("POST", '/api/v1'+url, true); // true for asynchronous 
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(data);

}

