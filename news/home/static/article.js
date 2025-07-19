var moon = document.querySelector('#moon')
let bd = document.querySelector('body')

moon.addEventListener('click',()=>{
    if (bd.classList.contains('dark_theme')){
        bd.classList.remove('dark_theme')
        moon.textContent='🌙';
    }
    else{
        bd.classList.add('dark_theme')
        moon.textContent='☀️'
        bd.style.transition='3s'
    }
})