document.getElementById("sendButton").addEventListener("click", function () {
    const btn = document.getElementById("sendButton");
    btn.style.pointerEvents = "none";
    btn.style.opacity = "0.6";

    // Captura todos os campos de código e quantidade
    const sections = document.querySelectorAll("section .form");
    const ItensReqCompra = [];
    let camposValidos = true;

    sections.forEach(formDiv => {
        const codInput = formDiv.querySelector('input[type="text"]');
        const qtdInput = formDiv.querySelector('input[type="number"]');
        const codItem = codInput ? codInput.value.trim() : "";
        const qtde = qtdInput ? qtdInput.value.trim() : "";

        if (!codItem || !qtde) {
            camposValidos = false;
        }

        ItensReqCompra.push({
            codItem: codItem,
            qtde: parseInt(qtde, 10)
        });
    });

    const obsReqCompra = document.getElementById("obs").value.trim();

    if (!camposValidos || !obsReqCompra) {
        alert("Por favor, preencha todos os campos!");
        btn.style.pointerEvents = "auto";
        btn.style.opacity = "1";
        return;
    }

    // Monta o payload final
    const payload = {
        obsReqCompra: obsReqCompra,
        ItensReqCompra: ItensReqCompra
    };

    fetch("https://192.168.88.72:5000/RequisicaoInclusaoCompra", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        window.location.href = "response.html";
    })
    .catch(error => {
        console.error("Erro:", error);
        alert("Ocorreu um erro ao enviar a requisição. Verifique os dados e tente novamente.");
        btn.style.pointerEvents = "auto";
        btn.style.opacity = "1";
    });
});

document.getElementById("MaisUm").addEventListener("click", function () {
    const separador = document.querySelector(".separador");
    const section = document.createElement("section");
    section.innerHTML = `
        <div class="form">
            <div>
                <p>
                    <input type="text" class="input" placeholder="Digite o código do item.">
                </p>
                <p>
                    <input type="number" class="input" placeholder="Digite a quantidade desejada.">
                </p>
            </div>
        </div>
    `;
    separador.parentNode.insertBefore(section, separador);
});