document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    validar_login();
 });

function validar_login() {
    const user = document.getElementById('user').value;
    const pass = document.getElementById('pass').value;

    if (user === 'admin' && pass === 'admin123') {
        alert('Login successful!');
        location.href = '/pagina1/site.html';
    } else if (user === '' || pass === '') {
        alert('Preencha todos os campos');
    } else {
        alert('Usuario e senha incorretos');
    }
}
