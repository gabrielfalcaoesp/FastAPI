var verificacao = 0; 

const selectElement = document.getElementById('unidadeSelect');
        selectElement.addEventListener('change', function() {
            const selectedValue = selectElement.value;
            console.log(selectedValue); // Aqui você pode fazer o que quiser com o valor selecionado
        });

const botaoAvancar = document.querySelector('.botaoAvancar');

selectElement.addEventListener('change', function() {
    const selectedValue = selectElement.value;

    if (selectedValue) {  
        botaoAvancar.style.cursor = 'pointer';
        verificacao = 1;
    } else {
        botaoAvancar.style.cursor = 'none';
    }
});

function redirectToPage() {
    if (verificacao==1) {  
    window.location.href = "agendamento_especialidade.html";
    }
  }