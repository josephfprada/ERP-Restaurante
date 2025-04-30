function sinProgramar(){
    alert("Está función todavía no ha sido programada");
}

function mostrarOpCli() {
    const ids = ['Cli1', 'Cli2', 'Cli3'];
    ids.forEach(id => {
        const div = document.getElementById(id);
        div.style.display = (div.style.display === 'block') ? 'none' : 'block';
    });
}

function mostrarOpPro() {
    const ids = ['Pro1', 'Pro2', 'Pro3'];
    ids.forEach(id => {
        const div = document.getElementById(id);
        div.style.display = (div.style.display === 'block') ? 'none' : 'block';
    });
}