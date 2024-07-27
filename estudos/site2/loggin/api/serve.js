//feito com ajuda de i.a
const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const connection = mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_DATABASE
});

connection.connect(err => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL');
});

app.post('/login', (req, res) => {
    const { user, pass } = req.body;

    if (!user || !pass) {
        return res.status(400).send('Preencha tudo');
    }

    const query = 'SELECT * FROM users WHERE username = ? AND password = ?';
    connection.query(query, [user, pass], (err, results) => {
        if (err) {
            console.error('Error executing query:', err);
            return res.status(500).send('Erro no servidor');
        }

        if (results.length > 0) {
            res.send('Login successful!');
        } else {
            res.status(401).send('Usuário ou senha incorretos');
        }
    });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
