menu = document.getElementsByClassName('menu')[0]
function abrirmenu(event){
    event.preventDefault()
    menu.classList.remove('fechado')
    menu.classList.add('aberto')
}
fm = document.getElementsByClassName('fm')[0]
function fecharmenu(event){
    event.preventDefault()
    menu.classList.add('fechado')
    menu.classList.remove('aberto')
}
