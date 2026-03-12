let selecionadas = [];
let letrasSelecionadas = [];
let palavrasRestantes = [];

let direcao = null;
let mousePressionado = false;
let inicio = null;

function gerarJogo() {

    const tema = document.getElementById("tema").value;

    fetch(`/jogo/${tema}`)
        .then(res => res.json())
        .then(data => {

            desenharTabuleiro(data.matriz);
            mostrarPalavras(data.palavras);

            // limpa estados
            limparSelecao();
            selecionadas = [];
            letrasSelecionadas = [];
        });
}

function iniciarJogo(){

    document.getElementById("tela-inicial").style.display = "none";

    document.getElementById("tela-jogo").style.display = "block";

}

function desenharTabuleiro(matriz) {
    const tabuleiro = document.getElementById("tabuleiro");
    tabuleiro.innerHTML = "";

    matriz.forEach((linha, i) => {
        const linhaDiv = document.createElement("div");
        linhaDiv.className = "linha";

        linha.forEach((letra, j) => {
            const celula = document.createElement("div");
            celula.className = "celula";
            celula.textContent = letra;

            celula.dataset.linha = i;
            celula.dataset.coluna = j;
//
           celula.addEventListener("mousedown", () => {
    limparSelecao();
    mousePressionado = true;
    inicio = celula;
    direcao = null;
    selecionarCelula(celula);
});

celula.addEventListener("mouseover", () => {
    if (!mousePressionado) return;

    const ultima = selecionadas[selecionadas.length - 1];
    if (!ehVizinha(ultima, celula)) {
        limparSelecao();
        mousePressionado = false;
        return;
    }

    selecionarCelula(celula);
});

            linhaDiv.appendChild(celula);
        });

        tabuleiro.appendChild(linhaDiv);
    });
}
function selecionarCelula(celula) {
    //evita selecionar a mesma celula mmais de uma vez
    if (selecionadas.includes(celula)) return;
    //evita selecionar letras ja encontradas
    if (celula.classList.contains("encontrada")) return;

    celula.classList.add("selecionada");
    selecionadas.push(celula);
    letrasSelecionadas.push(celula.textContent);
//aquiiiii
   // const palavra = letrasSelecionadas.join("");

    //verificarPalavra(palavra);
}
function mostrarPalavras(palavras) {
    const lista = document.getElementById("lista-palavras");
    lista.innerHTML = "";

    palavrasRestantes = palavras;

    palavras.forEach(palavra => {
        const li = document.createElement("li");
        li.textContent = palavra;
        li.id = palavra;
        lista.appendChild(li);
    });
}
//verificar se acertou
function verificarPalavra(palavra) {

    if (palavrasRestantes.includes(palavra)) {

        // marca células
        selecionadas.forEach(celula => {
            celula.classList.remove("selecionada");
            celula.classList.add("encontrada");
        });

        // risca palavra
        const li = document.getElementById(palavra);
        li.classList.add("riscada");

        // remove da lista
        palavrasRestantes = palavrasRestantes.filter(p => p !== palavra);

    } else{
         limparSelecao();
    }

    }

       
//limpar selecao
function limparSelecao() {
    selecionadas.forEach(celula => {
        celula.classList.remove("selecionada");
    });

    selecionadas = [];
    letrasSelecionadas = [];
}
function ehVizinha(a, b) {
    const l1 = parseInt(a.dataset.linha);
    const c1 = parseInt(a.dataset.coluna);
    const l2 = parseInt(b.dataset.linha);
    const c2 = parseInt(b.dataset.coluna);

    return (
        (l1 === l2 && Math.abs(c1 - c2) === 1) || // horizontal
        (c1 === c2 && Math.abs(l1 - l2) === 1)    // vertical
    );
}
document.addEventListener("mouseup", () => {
    if (mousePressionado) {
        verificarPalavra(letrasSelecionadas.join(""));
    }
    mousePressionado = false;
    inicio = null;
    direcao = null;
});