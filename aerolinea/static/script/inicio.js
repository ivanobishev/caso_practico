//-----[Ventana emergente]-----
var ventana_emergente = document.getElementById("ventana-emergente");
var close_button = document.getElementById("close-button");

close_button.addEventListener("click", function() {
    ventana_emergente.style.display = "none";
}, false);
window.onclick = function(event) {
    if(event.target == ventana_emergente) {
        ventana_emergente.style.display = "none";
    }
}

//-----[Detector de cambios]-----
const callback = (changeList, observer) => {
    console.log(changeList);
    //alert("A new flight has been added");
    ventana_emergente.style.display = "block";
}

const observer = new MutationObserver(callback);

document.onreadystatechange = () => {
    if(document.readyState === 'complete') {
        const elem = document.getElementById('main-table');
        observer.observe(elem, {
            subtree: true,
            childList: true
        })
    }
};

function starting()
{
    // Texto de prueba para añadir filas a la tabla.
    // Esto imitaría una actualización de la tabla, donde se añade otro vuelo.
    var main_table = document.getElementById("main-table");
    var add_button = document.getElementById("add-button");
    add_button.addEventListener("click", function() {
        var new_row = main_table.insertRow();
        for(let i = 0; i < 9; i++) {
            var new_cell = new_row.insertCell();
            var new_text = document.createTextNode('campo');
            new_cell.appendChild(new_text);
        }
    }, false);
}
window.onload = starting;
