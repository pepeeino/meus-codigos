function validate_site() {
  const input = document.getElementById("input").value;
  const output = document.getElementById("output");

  var xhr = new XMLHttpRequest();

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        output.textContent = `Response: ${xhr.status}`;
      } else {
        output.textContent = `Error: ${xhr.status}`;
      }
    }
  };

  xhr.open("GET", input, true);
  xhr.send();
  } catch (error) {
    output.textContent = `Error: ${error.message}`;
  }
}
