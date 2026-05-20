from pyswip import Prolog
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Conecta ao Prolog
prolog = Prolog()

prolog.consult("rede_social.pl")

# Carrega CSV
df = pd.read_csv("dados_financeiros.csv")

# Função que consulta o Prolog
def obter_grau_risco(nome):

    consulta = list(
        prolog.query(
            f"risco_conexao({nome}, daniel, Grau)"
        )
    )

    if consulta:
        return consulta[0]["Grau"]

    return 999

# Cria coluna usando Prolog
df["grau_risco_rede"] = df["cliente_id"].apply(
    obter_grau_risco
)

print("DataFrame:")
print(df)

# Features
X = df[[
    "renda_mensal",
    "score_classico",
    "grau_risco_rede"
]]

# Alvo
y = df["inadimplente_historico"]

# Modelo
modelo = LogisticRegression()

modelo.fit(X, y)

print("\nCoeficientes:")
print(modelo.coef_)

# Cliente novo
cliente_novo = pd.DataFrame({
    "renda_mensal": [2000],
    "score_classico": [450],
    "grau_risco_rede": [1]
})

prob = modelo.predict_proba(cliente_novo)[0][1]

print(f"\nProbabilidade de risco: {prob:.2f}")