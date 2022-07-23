(function () {

    const btnDelete = document.querySelectorAll(".btnDelete")

    btnDelete.forEach(btn => {
        btn.addEventListener('click',(e) => {
        const confirmacion = confirm('¿Are you sure you want to delete this data?');
        if(!confirmacion){
            e.preventDefault();
        }
        });
    });
})();