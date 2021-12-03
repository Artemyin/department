
var deleteItems = document.querySelectorAll('.js-delete-item');

// for (let i = 0; i < deleteItem.length - 1; i++) {
//     buttonItems[i].addEventListner('click', (e) => {

//         console.log('click is worked!')
//         const id = +e.currentTarget.dataset.id; // это твой айди на текущей кнопке 
//         const endpoint = e.currentTarget.dataset.endpoint
//         alert('hello, there');

//         $.ajax({
//         url : endpoint,
//         method : 'delete',
//         data : {id : id}
//         })
//     })
// }

for (let i = 0; i < deleteItems.length - 1; i++) {
    console.log('iteration!')
    deleteItems[i].addEventListner('click', (e) => {
      console.log('click is worked!')
      const id = e.currentTarget.dataset.id; // это твой айди на текущей кнопке 
    }
    )}
