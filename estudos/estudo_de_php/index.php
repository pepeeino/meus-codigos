<?php
include 'conexao.php';

$sql = "SELECT * FROM usuarios";
$resultado = $conexao->query($sql);
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Usuários</title>
</head>
<body>
    <h1>Lista de Usuários</h1>
    <a href="cadastro.php">Cadastrar Novo Usuário</a>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Email</th>
        </tr>
        <?php
        if ($resultado->num_rows > 0) {
            while ($usuario = $resultado->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $usuario['id'] . "</td>";
                echo "<td>" . $usuario['nome'] . "</td>";
                echo "<td>" . $usuario['email'] . "</td>";
                echo "</tr>";
            }
        } else {
            echo "<tr><td colspan='3'>Nenhum usuário encontrado</td></tr>";
        }
        ?>
    </table>
</body>
</html>
