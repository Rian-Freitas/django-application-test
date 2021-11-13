document.getElementById('clicaaqui').addEventListener('click', toggleDivs1);

function toggleDivs1() {
  var tela0 = document.getElementById('tela0');
  var tela1 = document.getElementById('tela1');
  var tela2 = document.getElementById('tela2');
  var tela3 = document.getElementById('tela3');
  var tela4 = document.getElementById('tela4');
  if (tela0.style.display != 'none') {
    tela0.style.display = 'none';
    tela1.style.display = 'inline';
    tela2.style.display = 'none';
    tela3.style.display = 'none';
    tela4.style.display = 'none';
  } else  if (tela1.style.display != 'none') {
    tela0.style.display = 'none';
    tela1.style.display = 'none';
    tela2.style.display = 'inline';
    tela3.style.display = 'none';
    tela4.style.display = 'none';
  } else  if (tela2.style.display != 'none') {
    tela0.style.display = 'none';
    tela1.style.display = 'none';
    tela2.style.display = 'none';
    tela3.style.display = 'inline';
    tela4.style.display = 'none';
  } else  if (tela3.style.display != 'none') {
    tela0.style.display = 'none';
    tela1.style.display = 'none';
    tela2.style.display = 'none';
    tela3.style.display = 'none';
    tela4.style.display = 'inline';
  } else {
    tela0.style.display = 'inline';
    tela1.style.display = 'none';
    tela2.style.display = 'none';
    tela3.style.display = 'none';
    tela4.style.display = 'none';
  }
}

document.getElementById('clicanao').addEventListener('click', toggleDivs2);

function toggleDivs2() {
  var skin0 = document.getElementById('skin0');
  var skin1 = document.getElementById('skin1');
  var skin2 = document.getElementById('skin2');
  var skin3 = document.getElementById('skin3');
  var skin4 = document.getElementById('skin4');
  if (skin0.style.display != 'none') {
    skin0.style.display = 'none';
    skin1.style.display = 'inline';
    skin2.style.display = 'none';
    skin3.style.display = 'none';
    skin4.style.display = 'none';
  } else if (skin1.style.display != 'none') {
    skin0.style.display = 'none';
    skin1.style.display = 'none';
    skin2.style.display = 'inline';
    skin3.style.display = 'none';
    skin4.style.display = 'none';
  } else if (skin2.style.display != 'none') {
    skin0.style.display = 'none';
    skin1.style.display = 'none';
    skin2.style.display = 'none';
    skin3.style.display = 'inline';
    skin4.style.display = 'none';
  } else if (skin3.style.display != 'none') {
    skin0.style.display = 'none';
    skin1.style.display = 'none';
    skin2.style.display = 'none';
    skin3.style.display = 'none';
    skin4.style.display = 'inline';
  } else {
    skin0.style.display = 'inline';
    skin1.style.display = 'none';
    skin2.style.display = 'none';
    skin3.style.display = 'none';
    skin4.style.display = 'none';
  }
}