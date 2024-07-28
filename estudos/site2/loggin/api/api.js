document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    validar_login();
 });

 function validar_login() {
    const user = document.getElementById('user').value;
    const pass = document.getElementById('pass').value;

    if (user === 'admin' && pass === 'admin123') {
        alert('Login successful!');
        location.href = './site.html';
    } else if (user === '' || pass === '') {
        alert('Preencha todos os campos');
    } else {
        alert('Usuario e senha incorretos');
    }
}    

/*tem q colocar return false no 'submit' se n ele n ira redirecionar para a outra pagina, mas 
mesmo se eu conseguisse colocar ele n iria funcionar pois o GET n esta funcionando corretamente*/