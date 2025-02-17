import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report

# 1. Carregar os dados (ajuste o nome do arquivo e das colunas conforme necessário)
df = pd.read_csv('dados.csv')  # O CSV deve conter, por exemplo, as colunas:
                                # 'descricao_transacao', 'segmento_cnpj', 'classificacao_N1', 'classificacao_N2'

# 2. Separar as features (X) e os rótulos (y)
X = df[['descricao_transacao', 'segmento_cnpj']]
y = df[['classificacao_N1', 'classificacao_N2']]

# 3. Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Construir o pré-processador para cada coluna:
# - Para a descrição, utiliza-se TfidfVectorizer para transformar o texto em vetores numéricos.
# - Para o segmento do CNPJ, utiliza-se OneHotEncoder para transformar a variável categórica.
preprocessor = ColumnTransformer(
    transformers=[
        ('descricao', TfidfVectorizer(), 'descricao_transacao'),
        ('segmento', OneHotEncoder(handle_unknown='ignore'), ['segmento_cnpj'])
    ]
)

# 5. Criar o pipeline completo com um classificador multi-saída:
# Utilizamos o MultiOutputClassifier que, internamente, treina um modelo (aqui, LogisticRegression)
# para cada uma das saídas (classificacao_N1 e classificacao_N2).
modelo = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classificador', MultiOutputClassifier(LogisticRegression(solver='lbfgs', max_iter=1000)))
])

# 6. Treinar o modelo
modelo.fit(X_train, y_train)

# 7. Avaliar o modelo
y_pred = modelo.predict(X_test)
print("Acurácia geral:", modelo.score(X_test, y_test))
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=['N1', 'N2']))
