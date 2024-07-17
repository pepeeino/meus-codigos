document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    validar_login();
});

function validar_login() {
    const user = document.getElementById('user').value;
    const pass = document.getElementById('pass').value;

    if (user === '' || pass === '') {
        alert('Preencha tudo');
    } else {
        // Perform login action
        alert('Login successful!');
    }
}
