# Sistema Híbrido de Análise de Risco com Prolog e Python

## Descrição

Este projeto implementa um sistema híbrido de análise de risco de crédito utilizando:

- Prolog para modelagem relacional
- Python para aprendizado estatístico
- Regressão Logística com Scikit-Learn
- Integração simbólica e probabilística (SRL)

O sistema utiliza:
- atributos financeiros tradicionais
- relações financeiras entre clientes
- inferência lógica para calcular risco relacional

---

# Estrutura do Projeto

IA_atividade/
│
├── rede_social.pl
├── dados_financeiros.csv
├── main.py
├── requirements.txt
├── HOWTO.md
└── README.md

---

# Tecnologias Utilizadas

- SWI-Prolog
- Python
- Pandas
- Scikit-Learn
- pyswip

---

# Instalação

## 1. Instalar o Python

Baixe o Python:
https://www.python.org/downloads/

---

## 2. Instalar o SWI-Prolog

Baixe o SWI-Prolog:
https://www.swi-prolog.org/download/stable

O pyswip precisa do SWI-Prolog instalado na máquina.

---

## 3. Instalar as bibliotecas Python

Abra o terminal na pasta do projeto e execute:

pip install pandas pyswip scikit-learn

Ou utilize:

pip install -r requirements.txt

---

# Execução

No terminal, execute:

python main.py

---

# Funcionamento do Projeto

## Parte Lógica (Prolog)

O arquivo `rede_social.pl` modela:
- conexões financeiras
- relações entre clientes
- propagação de risco

Exemplo:

joao -> ana -> carlos -> daniel

O sistema calcula o grau de proximidade entre clientes e indivíduos inadimplentes.

---

## Parte Estatística (Python)

O Python:
1. conecta ao Prolog utilizando pyswip
2. consulta os graus de risco
3. adiciona os dados ao DataFrame
4. treina uma Regressão Logística
5. calcula probabilidades de risco

---

# Exemplo de Saída

DataFrame:

cliente_id | renda_mensal | score_classico | inadimplente_historico | grau_risco_rede

joao | 5200 | 750 | 0 | 3

ana | 3100 | 610 | 0 | 2

carlos | 1800 | 420 | 1 | 1

---

Coeficientes:

[[-3.17564634e-02 -5.82047241e-03 1.54664186e-06]]

---

Probabilidade de risco:

1.00

---

# Objetivo Acadêmico

Demonstrar a integração entre:
- lógica simbólica
- inferência relacional
- aprendizado estatístico

Aplicando conceitos de Statistical Relational Learning (SRL).
