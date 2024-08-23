function validate_site() {
  const input = document.getElementById("input").value;
  const output = document.getElementById("output");

  fetch(input)
    .then((response) => {
      output.textContent = `Response: ${response.status}`;
    })
    .catch((error) => {
      output.textContent = `Error: ${error.message}`;
    });
}
