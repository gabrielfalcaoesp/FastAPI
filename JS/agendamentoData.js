var verificacao = 0; 

var amanha = document.getElementById('amanha');
  amanha.addEventListener('click', function(event) {
    divSelecionada = 1;
    if (event.target === amanha) {
        amanha.style['boxShadow'] = '-1px 0px 0px 2px #00ca65';
        outraData.style['boxShadow'] = '0px 0px 0px 0px #00ca65';
        depoisAmanha.style['boxShadow'] = '0px 0px 0px 0px #00ca65';
        verificacao = 1;
    }
  });

  var depoisAmanha = document.getElementById('depoisAmanha');
  depoisAmanha.addEventListener('click', function(event) {
    if (event.target === depoisAmanha) {
        amanha.style['boxShadow'] = '0px 0px 0px 0px #00ca65';
        outraData.style['boxShadow'] = '0px 0px 0px 0px #00ca65';
        depoisAmanha.style['boxShadow'] = '0px 0px 0px 1.5px #00ca65';
        verificacao = 1;
    }
  });

  var outraData = document.getElementById('outraData');
  outraData.addEventListener('click', function(event) {
    if (event.target === outraData) {
        amanha.style['boxShadow'] = '0px 0px 0px 0px #00ca65';
        depoisAmanha.style['boxShadow'] = '0px 0px 0px 0px #00ca65';
        outraData.style['boxShadow'] = '1px 0px 0px 2px #00ca65';
        verificacao = 1;
    }
  });

function redirectToPage() {
    if (verificacao==1) {  
    window.location.href = "agendamento_profissional.html";
    }
  }

// Função para obter a data de amanhã
   function obterDataAmanha() {
    var hoje = new Date();
    var amanha = new Date(hoje);
    amanha.setDate(hoje.getDate() + 1);
    return amanha;
}

// Função para formatar a data no formato desejado (dd)
function formatarData(data) {
    var dia = data.getDate();
    return dia;
}

// Função para obter a data depois de amanhã
function obterDataDepoisAmanha() {
  var hoje = new Date();
  var depois_amanha = new Date(hoje);
  depois_amanha.setDate(hoje.getDate() + 2);
  return depois_amanha;
}

// Função para formatar a data no formato desejado (dd)
function formatarData(data) {
  var dia = data.getDate();
  return dia;
}

document.getElementById('dataAmanha').textContent = formatarData(obterDataAmanha());
document.getElementById('DataDepoisAmanha').textContent = formatarData(obterDataDepoisAmanha());