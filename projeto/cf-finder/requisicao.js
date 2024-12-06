function ping_site() {
  const input = document.getElementById("site").value.trim();
  const output = document.getElementById("output");

  if (!input) {
    output.textContent = "Erro: Por favor, insira uma URL válida.";
    return;
  }

  // Adicionando validação simples de URL
  const urlPattern = /^(https?:\/\/)?[\w.-]+(\.[\w.-]+)+.*$/;
  if (!urlPattern.test(input)) {
    output.textContent = "Erro: URL inválida. Verifique o formato.";
    return;
  }

  const xhr = new XMLHttpRequest();

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        try {
          // Tentando acessar os cookies
          const cookies = document.cookie;

          // Verificando se o Cloudflare está presente nos cookies
          if (cookies.includes("cf")) {
            output.textContent = `Resposta: ${xhr.status} - Cookies do Cloudflare encontrados.`;

            // Verificando cookies JWT
            const jwtPattern =
              /(?:^|;)\s*(cf_clearance|__cfduid|jwt)\s*=\s*([^;]+)/i;
            const match = cookies.match(jwtPattern);

            if (match) {
              output.textContent += `\nCookie JWT encontrado: ${match[1]} = ${match[2]}`;
            } else {
              output.textContent += `\nNenhum cookie JWT encontrado.`;
            }
          } else {
            output.textContent = `Resposta: ${xhr.status} - Cookies do Cloudflare não encontrados.`;
          }
        } catch (error) {
          output.textContent = `Erro: Não foi possível acessar os cookies - ${error.message}`;
        }
      } else {
        output.textContent = `Erro na requisição: ${xhr.status} - ${
          xhr.statusText || "Problema desconhecido"
        }.`;
      }
    }
  };

  try {
    const url = input.startsWith("http") ? input : `http://${input}`;
    xhr.open("GET", url, true);
    xhr.send();
  } catch (error) {
    output.textContent = `Erro na requisição: ${error.message}`;
  }
}
