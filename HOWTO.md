# HOWTO - Sistema Híbrido de Análise de Risco

## Descrição do Projeto

Este projeto implementa um sistema híbrido de análise de risco de crédito utilizando:

- Prolog para modelagem relacional
- Python para aprendizado estatístico
- Regressão Logística com Scikit-Learn
- Integração simbólica e probabilística (SRL)

O objetivo é identificar o risco de inadimplência utilizando:
- atributos financeiros tradicionais
- relações sociais e financeiras entre clientes

---

# Estrutura do Projeto

IA_atividade/
│
├── rede_social.pl
├── dados_financeiros.csv
├── main.py
├── requirements.txt
└── HOWTO.md

---

# Arquivos

## rede_social.pl

Arquivo responsável pela base lógica em Prolog.

Contém:
- relações financeiras
- conexões entre clientes
- regras recursivas de propagação de risco

---

## dados_financeiros.csv

Base de dados financeira utilizada pelo Python.

Contém:
- renda mensal
- score de crédito
- histórico de inadimplência

---

## main.py

Script principal do projeto.

Responsável por:
1. conectar ao Prolog via pyswip
2. consultar os graus de risco
3. gerar a feature relacional
4. treinar a regressão logística
5. calcular probabilidades de risco

---

# Instalação

## Instalar dependências

pip install -r requirements.txt

---

# Execução

Executar o arquivo principal:

python main.py

---

# Funcionamento do Sistema

## Parte Lógica (Prolog)

O Prolog modela as relações financeiras entre indivíduos.

Exemplo:

joao -> ana -> carlos -> daniel

O sistema calcula recursivamente o grau de proximidade entre clientes e indivíduos inadimplentes.

---

## Parte Estatística (Python)

O Python:
- consulta o Prolog
- obtém o grau de risco relacional
- adiciona os dados ao DataFrame
- treina uma Regressão Logística

---

# Resultado Esperado

O sistema exibe:

- DataFrame enriquecido com risco relacional
- coeficientes aprendidos pelo modelo
- probabilidade de risco para novos clientes

Exemplo:

Probabilidade de risco: 1.00

---

# Tecnologias Utilizadas

- SWI-Prolog
- Python
- Pandas
- Scikit-Learn
- pyswip

---

# Objetivo Acadêmico

Demonstrar a integração entre:
- lógica simbólica
- inferência relacional
- aprendizado estatístico

Aplicando conceitos de Statistical Relational Learning (SRL).
