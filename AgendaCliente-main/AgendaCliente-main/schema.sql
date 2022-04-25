DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL,
    sexo TEXT ,
    servico TEXT,
    data DATE,
    horario TIME,
    content TEXT NOT NULL
);	

