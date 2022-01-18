document.addEventListener('DOMContentLoaded', function() {  // open DOM of the page
    const deleteItems = document.querySelectorAll('.js-delete-item'); // node list of all buttons 
    Array.prototype.forEach.call(deleteItems, (item) => { // create array of delete buttons and assign function
        item.addEventListener('click', (e) => {  // call function when click
        var id = +e.currentTarget.dataset.id;  // get id from data-id property
        const endpoint = e.currentTarget.dataset.endpoint; // get endpoint from data-enpoint property
        var orphan = document.getElementById('del-dep'+id);
        if (endpoint == '/departments/'){
            if (orphan.checked){
		        id = id + '?orphan=1';
	        }
	        else{
		    id = id + '?orphan=0';
	        }
        }
        row = e.currentTarget.closest('tr')
        httpDeleteAsync(endpoint, id, row) // call function which send request
         
        
        })
    })
});


document.addEventListener('DOMContentLoaded', function() {
    const editItems = document.querySelectorAll('.js-edit-item');
    Array.prototype.forEach.call(editItems, (item) => { // create array of delete buttons and assign function
    item.addEventListener('click', (e) => {  // call function when click
        const id = +e.currentTarget.dataset.id;  // get id from data-id property
        const endpoint = e.currentTarget.dataset.endpoint; // get endpoint from data-enpoint property
        const form = document.querySelector('#edit'+id)
        if (endpoint == "/departments/") {
            const name = form.elements['name'].value
            var data = {"name": name}
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
        }
        const jsondata = JSON.stringify(data)
        httpPutAsync(endpoint, id, jsondata)

        // document.location.reload(true)
        })
    })
});


document.addEventListener('DOMContentLoaded', function() {
    const AddDepItems = document.querySelector('#AddDepButton');   
    if (AddDepItems != null) {    
    AddDepItems.addEventListener('click', (e) => {  // call function when click
        const form = document.querySelector('#AddDep')
        const name = form.elements['name'].value  
        const data = {"name": name}
        const jsondata = JSON.stringify(data)
        httpPostAsync('/departments/', jsondata)
        document.location.reload(true)
        // e.preventDefault();
    });
    }
});
    
    
document.addEventListener('DOMContentLoaded', function() {
    const AddEmpItems = document.querySelector('#AddEmpButton');

    AddEmpItems.addEventListener('click', (e) => { 
        const form = document.querySelector('#AddEmp')
        const name = form.elements['name'].value  
        const birthdate = form.elements['birthdate'].value
        const salary = form.elements['salary'].value
        var department = form.elements['department'].value
        if (department == '') {
            department = null
        }
        const data = {
            "name": name,
            "birthdate": birthdate,
            "salary": salary,
            "department": department,
            }
        const jsondata = JSON.stringify(data)
        httpPostAsync('/employees/', jsondata)

        // document.location.reload(true)
    });
});
function make_raw(id, name, salary, count){
var row_dep_table = `<tr>` +
            `<td>${id}</td>`+
            `<td><a href="/departments/${id}" id="department_name${id}">${name}</a></td>`+
            `<td>${salary}</td>`+
            `<td>${count}</td>`+
            `<td></td>`};

function httpDeleteAsync(url, id, e) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 204){
            // remove row from table with deleted data
            e.remove();
        };
    }
    xmlHttp.open("DELETE", '/api/v1'+url+id, true); // true for asynchronous 
    xmlHttp.send(null);
};


function httpPutAsync(url, id, data, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 ){
            const response = JSON.parse(xmlHttp.response);
            console.log("new", response.name)
            const department_name = document.getElementById('department_name'+response.id);
            department_name.textContent = response.name;
        };
    }
    xmlHttp.open("PUT", '/api/v1'+url+id, true); // true for asynchronous 
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(data);
};


function httpPostAsync(url, data)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 204){
            const response = JSON.parse(xmlHttp.response);

        };
    }
    xmlHttp.open("POST", '/api/v1'+url, true); // true for asynchronous 
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(data);
};

