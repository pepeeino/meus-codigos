function validate_site() {
  const input = document.getElementById("input").value;
  const output = document.getElementById("output");

  var xhr = new XMLHttpRequest();

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        // Tenta acessar os cookies se possível
        try {
          const cookies = document.cookie;
          if (cookies.includes("cf")) {
            output.textContent = `Response: ${xhr.status} - cloudflare cookies encontrados`;
          } else {
            output.textContent = `Response: ${xhr.status} - cookies não encontrados`;
          }
        } catch (error) {
          output.textContent = `Response: ${xhr.status} - não é possivel acessar`;
        }
      } else {
        output.textContent = `Error: ${xhr.status}`;
      }
    }
  };

  xhr.open("GET", input, true);
  xhr.send();
}
