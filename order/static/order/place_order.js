let BACKDROP = document.querySelector('.backdrop')
let MODAL = document.querySelector('.modal')
let PLACEORDER = document.querySelector('.submit_placeorder')


PLACEORDER.addEventListener('click', () => {
    BACKDROP.style.display = 'block'
    MODAL.style.display = 'block'
})