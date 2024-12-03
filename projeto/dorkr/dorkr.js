"google custom search:";
/*const API_KEY = "SUA_CHAVE_DE_API";
const CX = "SEU_CX";

function processInput() {
  const dorkInput = document.getElementById("dorkInput").value;
  const fileInput = document.getElementById("fileInput").files[0];

  if (dorkInput) {
    searchDork(dorkInput);
  } else if (fileInput) {
    const reader = new FileReader();
    reader.onload = function (event) {
      const fileContent = event.target.result;
      const dorks = fileContent
        .split("\n")
        .map((line) => line.trim())
        .filter((line) => line.length > 0);
      searchMultipleDorks(dorks);
    };
    reader.readAsText(fileInput);
  } else {
    displayOutput("Por favor, insira um dork ou selecione um arquivo.");
  }
}

function searchDork(dork) {
  const url = https://www.googleapis.com/customsearch/v1?q=${encodeURIComponent(
    dork
  )}&key=${API_KEY}&cx=${CX};

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const results = data.items || [];
      displayResults(results);
    })
    .catch((error) => {
      displayOutput("Erro ao buscar na web.");
      console.error(error);
    });
}

function searchMultipleDorks(dorks) {
  const results = [];
  let processedCount = 0;

  dorks.forEach((dork) => {
    searchDork(dork);
  });
}

function displayResults(results) {
  const output = document.getElementById("output");
  output.innerHTML = "";

  if (results.length === 0) {
    output.textContent = "Nenhum resultado encontrado.";
    return;
  }

  results.sort((a, b) => a.link.localeCompare(b.link));

  results.forEach((result) => {
    const resultElement = document.createElement("div");
    resultElement.classList.add("result");
    resultElement.innerHTML = 
      <a href="${result.link}" target="_blank">${result.title}</a>
      <p>${result.snippet}</p>
    ;
    output.appendChild(resultElement);
  });

  document.getElementById("downloadBtn").style.display = "block";

  window.searchResults = results;
}

function downloadResults() {
  const results = window.searchResults;
  const fileContent = results
    .map((result) => ${result.title}\n${result.link}\n)
    .join("\n");

  const blob = new Blob([fileContent], { type: "text/plain" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "resultados_dork.txt";
  a.click();
  URL.revokeObjectURL(url);
}

function displayOutput(message) {
  const output = document.getElementById("output");
  output.textContent = message;
}
*/

"bing search api:";
/*const API_KEY = "SUA_CHAVE_DE_API"; // Insira sua chave da Bing Search API aqui
const ENDPOINT = "https://api.cognitive.microsoft.com/bing/v7.0/search";

function processInput() {
  const dorkInput = document.getElementById("dorkInput").value;
  const fileInput = document.getElementById("fileInput").files[0];

  if (dorkInput) {
    searchDork(dorkInput);
  } else if (fileInput) {
    const reader = new FileReader();
    reader.onload = function (event) {
      const fileContent = event.target.result;
      const dorks = fileContent
        .split("\n")
        .map((line) => line.trim())
        .filter((line) => line.length > 0);
      searchMultipleDorks(dorks);
    };
    reader.readAsText(fileInput);
  } else {
    displayOutput("Por favor, insira um dork ou selecione um arquivo.");
  }
}

function searchDork(dork) {
  const url = `${ENDPOINT}?q=${encodeURIComponent(dork)}`;

  fetch(url, {
    method: "GET",
    headers: {
      "Ocp-Apim-Subscription-Key": API_KEY, // Chave de API da Bing Search
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const results = data.webPages.value || [];
      displayResults(results);
    })
    .catch((error) => {
      displayOutput("Erro ao buscar na web.");
      console.error(error);
    });
}

function searchMultipleDorks(dorks) {
  const results = [];
  let processedCount = 0;

  dorks.forEach((dork) => {
    searchDork(dork);
  });
}

function displayResults(results) {
  const output = document.getElementById("output");
  output.innerHTML = "";

  if (results.length === 0) {
    output.textContent = "Nenhum resultado encontrado.";
    return;
  }

  results.sort((a, b) => a.url.localeCompare(b.url)); // Organizando pelos links

  results.forEach((result) => {
    const resultElement = document.createElement("div");
    resultElement.classList.add("result");
    resultElement.innerHTML = `
      <a href="${result.url}" target="_blank">${result.name}</a>
      <p>${result.snippet}</p>
    `;
    output.appendChild(resultElement);
  });

  document.getElementById("downloadBtn").style.display = "block";

  window.searchResults = results; // Guardar os resultados para o download
}

function downloadResults() {
  const results = window.searchResults;
  const fileContent = results
    .map((result) => `${result.name}\n${result.url}\n`)
    .join("\n");

  const blob = new Blob([fileContent], { type: "text/plain" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "resultados_dork.txt";
  a.click();
  URL.revokeObjectURL(url);
}

function displayOutput(message) {
  const output = document.getElementById("output");
  output.textContent = message;
}
*/
