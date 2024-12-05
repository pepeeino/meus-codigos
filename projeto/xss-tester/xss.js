const form = document.getElementById("inputForm");
const outputDiv = document.getElementById("responseOutput");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const userInput = document.getElementById("urlField").value;

  try {
    const response = await fetch(
      "http://127.0.0.1:5000/projeto/xss-tester/request.py", //here you gonna put where are your request.py,where did you save it//

      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: userInput }), // Envia o URL para o servidor
      }
    );

    const data = await response.json();
    if (data.status === "success") {
      outputDiv.innerText = data.result;
    } else {
      outputDiv.innerText = `Erro: ${data.message}`;
    }
  } catch (error) {
    outputDiv.innerText = `Erro ao conectar ao servidor: ${error.message}`;
  }
});
