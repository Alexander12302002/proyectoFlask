const menu = document.querySelector("#menu");
const abrir = document.querySelector("#abrir");
const cerrar = document.querySelector("#cerrar");
const opcionesMenu = document.querySelectorAll(".opciones_menu a");

abrir.addEventListener("click", () => {
    menu.classList.add("visible");
});

cerrar.addEventListener("click", () => {
    menu.classList.remove("visible");
});

opcionesMenu.forEach(opcion => {
    opcion.addEventListener("click", () => {
        menu.classList.remove("visible"); 
    });
});