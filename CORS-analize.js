const fs = require('fs');

// Função para analisar a resposta e dar um veredito
function analisarResposta(resposta) {
  // Verificando o código de status HTTP
  if (resposta.statusCode === 200) {
    console.log('Status: OK (200) - A resposta foi bem-sucedida.');
  } else if (resposta.statusCode === 301 || resposta.statusCode === 302) {
    console.log('Status: Redirecionamento (301/302) - A página foi redirecionada.');
  } else {
    console.log(`Status: ${resposta.statusCode} - Possível erro na resposta.`);
  }

  // Verificando se a resposta contém a palavra "CORS"
  if (resposta.body.includes('CORS')) {
    console.log('Possível vulnerabilidade CORS detectada. Verifique a configuração de segurança.');
  }

  // Verificando erros na resposta (palavra "error" no corpo)
  if (resposta.body.includes('error')) {
    console.log('Erro detectado na resposta. Verifique o conteúdo para mais detalhes.');
  }

  // Analisando possíveis falhas de segurança
  if (resposta.body.includes('X-Frame-Options') || resposta.body.includes('X-XSS-Protection')) {
    console.log('Verifique se os cabeçalhos de segurança como X-Frame-Options e X-XSS-Protection estão configurados corretamente.');
  }

  // Adicionando um veredito final com base nas observações
  console.log('\n----- Veredito Final -----');
  if (resposta.statusCode === 200 && !resposta.body.includes('error')) {
    console.log('Resposta está OK e não contém erros evidentes.');
  } else {
    console.log('Possíveis problemas encontrados. Verifique a resposta para mais detalhes.');
  }
}

// Lê o arquivo da resposta (substitua pelo caminho do seu arquivo)
fs.readFile('/resposta.html', 'utf8', (err, data) => {
  if (err) {
    console.error('Erro ao ler o arquivo:', err);
    return;
  }

  // Exemplo de estrutura de resposta
  const resposta = {
    statusCode: 200,  // Exemplo de status, altere conforme necessário
    body: data,
  };

  // Analisando a resposta
  analisarResposta(resposta);
});
