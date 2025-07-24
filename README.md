# 🥊 UFC Fight Outcome Predictor

Este projeto utiliza machine learning para prever o vencedor de uma luta de MMA (UFC) com base em dados históricos e estatísticas dos lutadores. Os dados são obtidos automaticamente do [Kaggle](https://www.kaggle.com/datasets/mdabbert/ultimate-ufc-dataset) e tratados para alimentar modelos como **Random Forest** e **MLP (rede neural)**, além de usar **interpretação com SHAP**.

## 📊 Funcionalidades

- Download automático do dataset com `kagglehub`
- Limpeza e redução de colunas irrelevantes (de 118 para 19)
- Visualizações de correlação, distribuições e relações entre atributos
- Treinamento e ajuste de hiperparâmetros para:
  - Random Forest
  - MLPClassifier (Rede Neural)
- Avaliação com acurácia e importância das variáveis
- Interpretação com SHAP para explicar predições
- Simulações de lutas reais: ex: Charles Oliveira vs. Ilia Topuria

## 🧠 Modelos

| Modelo         | Acurácia |
|----------------|----------|
| Random Forest  | ~61%     |
| MLP (Rede Neural) | ~61%  |

## 📁 Requisitos

- Python 3.8+
- Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib
- SHAP
- kagglehub

Instale com:

```bash
pip install pandas numpy scikit-learn seaborn matplotlib shap kagglehub
```

## 🧪 Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/ufc-predictor.git
   cd ufc-predictor
   ```
2. Execute o script:
   ```bash
   python ams_andré.py
   ```

## 🧮 Exemplo de Simulação

```python
# Simular luta entre Charles Oliveira e Ilia Topuria
prediction = rf_model.predict(novo_df)
print(prediction)  # 1 (Azul vence) ou -1 (Vermelho vence)
```

## 📌 Observações

- A classificação do vencedor é representada por:
  - `1`: Blue corner vence
  - `-1`: Red corner vence
  - `0`: Empate ou sem vencedor

- Colunas como altura, idade, sequências de vitórias, vitórias por nocaute/submissão foram levadas em consideração.

## 📈 Interpretação com SHAP

O projeto inclui análise de importância das features e explicações individuais com gráficos SHAP.
