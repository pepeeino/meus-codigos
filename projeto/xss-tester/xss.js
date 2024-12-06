document
  .getElementById("uploadForm")
  .addEventListener("submit", async (event) => {
    event.preventDefault();

    const urlField = document.getElementById("urlField").value;
    const fileInput = document.getElementById("fileInput").files[0];
    const outputDiv = document.getElementById("output");

    if (!fileInput) {
      outputDiv.innerText = "Por favor, carregue um arquivo de payloads.";
      return;
    }

    try {
      // Lendo o conteúdo do arquivo
      const fileContent = await fileInput.text();

      const response = await fetch("http://127.0.0.1:5000/process", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          input: urlField,
          payloads: fileContent.split("\n").filter((line) => line.trim()),
        }),
      });

      const data = await response.json();
      outputDiv.innerText =
        data.status === "success"
          ? JSON.stringify(data.result, null, 2)
          : `Erro: ${data.message}`;
    } catch (error) {
      outputDiv.innerText = `Erro ao conectar ao servidor: ${error.message}`;
    }
  });
