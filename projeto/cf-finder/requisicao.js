/*function validate_site() {
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
}*/

function ping_site() {
  const input = document.getElementById("site").value.trim();
  const output = document.getElementById("output");

  if (!input) {
    output.textContent = "Error: Por favor, insira uma URL.";
    return;
  }

  // Validação simples de URL
  const urlPattern = /^(https?:\/\/)?[\w.-]+(\.[\w\.-]+)+.*$/;
  if (!urlPattern.test(input)) {
    output.textContent = "Error: URL inválida. Verifique o formato.";
    return;
  }

  const xhr = new XMLHttpRequest();

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status >= 200 && xhr.status < 300) {
        output.textContent = `Ping bem-sucedido: ${xhr.status}`;
      } else {
        output.textContent = `Erro no ping: ${xhr.status} - ${xhr.statusText}`;
      }
    }
  };

  try {
    // Corrigindo para 'HEAD'
    const url = input.startsWith("http") ? input : `http://${input}`;
    xhr.open("HEAD", url, true);
    xhr.send();
  } catch (error) {
    output.textContent = `Error: ${error.message}`;
  }
}
