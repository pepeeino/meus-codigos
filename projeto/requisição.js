function validate_site() {
  const input = document.getElementById("input").value;
  const resultado = document.getElementById("resultado");

  fetch("input")
    .then((response) => {
      resultado.textContent = `Response: ${response.status}`;
    })
    .catch((error) => {
      resultado.textContent = `Error: ${error.message}`;
    });
}
