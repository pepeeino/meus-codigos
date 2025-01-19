<?php
include 'conexao.php'; 

$nome = $_POST['nome']; 
$email = $_POST['email']; 

$sql = "INSERT INTO usuarios (nome, email) VALUES ('$nome', '$email')";

if ($conexao->query($sql) === TRUE) {
    echo "Usuário cadastrado com sucesso!";
} else {
    echo "Erro ao cadastrar: " . $conexao->error;
}

$conexao->close(); 
?>
<br><a href="cadastro.php">Voltar</a>