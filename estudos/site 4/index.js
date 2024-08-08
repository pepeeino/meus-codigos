document.getElementById("somar").addEventListener("click", function () {
  var numero1 = parseFloat(document.getElementById("numero1").value);
  var numero2 = parseFloat(document.getElementById("numero2").value);
  var resultado = numero1 + numero2;

  document.getElementById("resultado").textContent = "Resultado: " + resultado;

  document
    .getElementById("resultado")
    .setAttribute("data-resultado", resultado);
});

document
  .getElementById("resultado")
  .addEventListener("DOMSubtreeModified", function () {
    var resultado = document
      .getElementById("resultado")
      .getAttribute("data-resultado");

    if (resultado == "1234") {
      alert("aqueles q partiram sempre estarão conosco");
    } else {
      alert("i love math");
    }
  });
