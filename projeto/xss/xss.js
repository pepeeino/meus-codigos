function enviarDados() {
  const input = document.getElementById("site").value.trim();

  if (!input) {
    alert("Por favor, insira uma URL.");
    return;
  }

  fetch('http://127.0.0.1:5000/projeto/xss-tester/endpoint.py', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url: input }),
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Erro do servidor: ${response.status} - ${response.statusText}`);
      }
      return response.json();
    })
    .then(data => {
      console.log("Resposta do servidor:", data);
      const output = document.getElementById("output");
      output.textContent = data.message; // Exibe a resposta no frontend
    })
    .catch(error => {
      console.error("Erro ao conectar ao servidor:", error);
      alert(`Erro ao conectar ao servidor: ${error.message}`);
    });
}
