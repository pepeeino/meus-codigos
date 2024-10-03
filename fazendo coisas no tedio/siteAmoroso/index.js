let simClickCount = 0;

var simButtons = document.getElementsByClassName("respostas");

for (var i = 0; i < simButtons.length; i++) {
  simButtons[i].onclick = function () {
    if (this.textContent.toLowerCase() === "sim") {
      simClickCount++;
      if (simClickCount < 3) {
        alert("Você está sendo modesto ou está mentindo...");
      } else {
        alert("Ok, eu também te amo muito!");
      }
    } else if (this.textContent.toLowerCase() === "não") {
      mostrarCaixa();
    }
  };
}

function mostrarCaixa() {
  var div = document.createElement("div");
  div.className = "alert-box";
  div.innerHTML = "...";

  document.body.appendChild(div);

  setTimeout(function () {
    document.body.removeChild(div);
  }, 2000);
}
