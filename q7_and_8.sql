-- Q7
CREATE TABLE stg_prontuario.Atendimento(
    id VARCHAR,
    dt_atendimento DATE,
    CONSTRAINT atendimento_pk PRIMARY KEY(id)
);

CREATE TABLE stg_prontuario.Diagnostico(
    id VARCHAR,
    id_atendimento VARCHAR,
    CONSTRAINT diagnostico_pk PRIMARY KEY(id),
    CONSTRAINT diagnostico_atendimento_fk FOREIGN KEY(id_atendimento) REFERENCES stg_prontuario.Atendimento(id)
);

-- Q8

ALTER TABLE stg_prontuario.Atendimento
ADD tipo_atendimento CHAR;

SELECT AVG(COUNT(D.id)) AS media_diagnosticos
FROM stg_prontuario.Atendimento A
    LEFT JOIN stg_prontuario.Diagnostico D 
        ON A.id = D.id_atendimento
WHERE A.tipo_atendimento = 'U'
GROUP BY A.id;
