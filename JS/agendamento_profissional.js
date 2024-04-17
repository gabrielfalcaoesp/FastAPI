// Função para selecionar o horário
function associarHorario(elementoClicado) {
    // Remove a classe "selecionada" de todas as caixas
    var todasCaixas = document.querySelectorAll('.caixa');
    todasCaixas.forEach(function(caixa) {
        caixa.classList.remove('selecionada');
    });

    // Adiciona a classe "selecionada" à caixa clicada
    elementoClicado.classList.add('selecionada');
}