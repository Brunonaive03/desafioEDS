
-- Q1

CREATE TABLE stg_prontuario.Paciente(
    id INT, -- identificador único sequencial
    nome VARCHAR, -- nome do paciente
    dt_nascimento DATE, -- data de nascimento do paciente
    cpf INT, -- CPF do paciente
    nome_mae VARCHAR, -- nome da mãe do paciente
    dt_atualizacao TIMESTAMP, -- data e hora de atualização do paciente
    CONSTRAINT paciente_pk PRIMARY KEY(id)
);

-- Q2

CREATE SEQUENCE prontuario_paciente_seq START WITH 1 INCREMENT BY 1;

INSERT INTO stg_prontuario.Paciente (id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao)
SELECT prontuario_paciente_seq.NEXTVAL, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao
FROM(
SELECT nome, dt_nascimento, cpf, nome_mae, dt_atualizacao FROM stg_hospital_a.Paciente
UNION ALL
SELECT nome, dt_nascimento, cpf, nome_mae, dt_atualizacao FROM stg_hospital_b.Paciente
UNION ALL
SELECT nome, dt_nascimento, cpf, nome_mae, dt_atualizacao FROM stg_hospital_c.Paciente;
);

-- Q3

SELECT *
FROM stg_prontuario.Paciente P
WHERE P.cpf IN (
    SELECT P2.cpf
    FROM stg_prontuario.Paciente P2
    GROUP BY P2.cpf
    HAVING COUNT(*) > 1 
)

-- Q4

SELECT *
FROM stg_prontuario.Paciente P
WHERE (P.cpf, P.dt_atualizacao) IN (
    SELECT P2.cpf, MAX(P2.dt_atualizacao)
    FROM stg_prontuario.Paciente P2
    GROUP BY P2.cpf
    HAVING COUNT(*) > 1 
)

