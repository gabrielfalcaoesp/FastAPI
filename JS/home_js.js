console.log("teste");

function exibirLogin() {
    var container = document.querySelector('.caixa');
    var computedStyle = window.getComputedStyle(container);
  
    if (computedStyle.display === 'none') {
      container.style.display = 'block';
      console.log("O estado do display é: block")
    } else {
      container.style.display = 'none';
      console.log("O estado do display é: none")
    }
    
  }

const clicouDentro = document.querySelector('.BL img');
const clicouDentroCaixa = document.querySelector('.caixa');
document.addEventListener('mousedown', (event) => {
  if (clicouDentro.contains(event.target) || clicouDentroCaixa.contains(event.target)) {
  } else {
    var container = document.querySelector('.caixa');
    container.style.display = 'none';
  }
})
