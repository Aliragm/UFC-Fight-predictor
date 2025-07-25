# -*- coding: utf-8 -*-
"""AMS_André.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dfz526rlXKosfsP8QMqJz52RNRcpubBp
"""

import kagglehub
import pandas as pd
import os

path = kagglehub.dataset_download("mdabbert/ultimate-ufc-dataset")

files = os.listdir(path)

csv_file = [f for f in files if f.endswith(".csv")][1]
csv_file_upcoming = [f for f in files if f.endswith(".csv")][0]
csv_path = os.path.join(path, csv_file)

csv_path_upcoming = os.path.join(path, csv_file_upcoming )

df_upcoming = pd.read_csv(csv_path_upcoming)

df = pd.read_csv(csv_path)

df

df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")

df = df[df["Date"] >= pd.to_datetime("2017-01-01")]

df

"""Colunas que irei eliminar

RedExpectedValue
BlueExpectedValue
Gender
RedAge
BlueAge
BlueCurrentLoseStreak
BlueCurrentWinStreak
BlueDraws
BlueAvgSigStrLanded
BlueAvgSigStrPct
BlueAvgSubAtt
BlueAvgTDLanded
BlueAvgTDPct
BlueLongestWinStreak
BlueLosses
BlueTotalRoundsFought
BlueTotalTitleBouts
BlueWinsByDecisionMajority
BlueWinsByDecisionSplit
BlueWinsByDecisionUnanimous
BlueWinsByKO
BlueWinsBySubmission
BlueWinsByTKODoctorStoppage
BlueWins
BlueStance
BlueHeightCms
BlueReachCms
BlueWeightLbs
RedCurrentLoseStreak
RedCurrentWinStreak
RedDraws
RedAvgSigStrLanded
RedAvgSigStrPct
RedAvgSubAtt
RedAvgTDLanded
RedAvgTDPct
RedLongestWinStreak
RedLosses
RedTotalRoundsFought
RedTotalTitleBouts
RedWinsByDecisionMajority
RedWinsByDecisionSplit
RedWinsByDecisionUnanimous
RedWinsByKO
RedWinsBySubmission
RedWinsByTKODoctorStoppage
RedWins
RedStance
RedHeightCms
RedReachCms
RedWeightLbs
BMatchWCRank
RMatchWCRank
RWFlyweightRank
RWFeatherweightRank
RWStrawweightRank
RWBantamweightRank
RHeavyweightRank
RLightHeavyweightRank
RMiddleweightRank
RWelterweightRank
RLightweightRank
RFeatherweightRank
RBantamweightRank
RFlyweightRank
RPFPRank
BWFlyweightRank
BWFeatherweightRank
BWStrawweightRank
BWBantamweightRank
BHeavyweightRank
BLightHeavyweightRank
BMiddleweightRank
BWelterweightRank
BLightweightRank
BFeatherweightRank
BBantamweightRank
BFlyweightRank
BPFPRank
Finish
FinishDetails
FinishRound
FinishRoundTime
TotalFightTimeSecs
RedDecOdds
BlueDecOdds
RSubOdds
BSubOdds
RKOOdds
BKOOdds
RedOdds
BlueOdds
RedExpectedValue
BlueExpectedValue
"""

df_clean = df.drop([
    "RedExpectedValue", "BlueExpectedValue", "Gender", "RedAge", "BlueAge",
    "BlueCurrentLoseStreak", "BlueCurrentWinStreak", "BlueDraws", "BlueAvgSigStrLanded",
    "BlueAvgSigStrPct", "BlueAvgSubAtt", "BlueAvgTDLanded", "BlueAvgTDPct",
    "BlueLongestWinStreak", "BlueLosses", "BlueTotalRoundsFought", "BlueTotalTitleBouts",
    "BlueWinsByDecisionMajority", "BlueWinsByDecisionSplit", "BlueWinsByDecisionUnanimous",
    "BlueWinsByKO", "BlueWinsBySubmission", "BlueWinsByTKODoctorStoppage", "BlueWins",
    "BlueStance", "BlueHeightCms", "BlueReachCms", "BlueWeightLbs",
    "RedCurrentLoseStreak", "RedCurrentWinStreak", "RedDraws", "RedAvgSigStrLanded",
    "RedAvgSigStrPct", "RedAvgSubAtt", "RedAvgTDLanded", "RedAvgTDPct",
    "RedLongestWinStreak", "RedLosses", "RedTotalRoundsFought", "RedTotalTitleBouts",
    "RedWinsByDecisionMajority", "RedWinsByDecisionSplit", "RedWinsByDecisionUnanimous",
    "RedWinsByKO", "RedWinsBySubmission", "RedWinsByTKODoctorStoppage", "RedWins",
    "RedStance", "RedHeightCms", "RedReachCms", "RedWeightLbs",
    "BMatchWCRank", "RMatchWCRank",
    "RWFlyweightRank", "RWFeatherweightRank", "RWStrawweightRank", "RWBantamweightRank",
    "RHeavyweightRank", "RLightHeavyweightRank", "RMiddleweightRank", "RWelterweightRank",
    "RLightweightRank", "RFeatherweightRank", "RBantamweightRank", "RFlyweightRank",
    "RPFPRank", "BWFlyweightRank", "BWFeatherweightRank", "BWStrawweightRank",
    "BWBantamweightRank", "BHeavyweightRank", "BLightHeavyweightRank", "BMiddleweightRank",
    "BWelterweightRank", "BLightweightRank", "BFeatherweightRank", "BBantamweightRank",
    "BFlyweightRank", "BPFPRank",
    "Finish", "FinishDetails", "FinishRound", "FinishRoundTime", "TotalFightTimeSecs",
    "RedDecOdds", "BlueDecOdds", "RSubOdds", "BSubOdds", "RKOOdds", "BKOOdds",
    "RedOdds", "BlueOdds", "RedExpectedValue", "BlueExpectedValue", "EmptyArena", "RedFighter", "BlueFighter", "Date", "Location", "Country", "BetterRank"
], axis=1)
df_clean

df_upcoming_clean = df_upcoming.drop([
    "RedExpectedValue", "BlueExpectedValue", "Gender", "RedAge", "BlueAge",
    "BlueCurrentLoseStreak", "BlueCurrentWinStreak", "BlueDraws", "BlueAvgSigStrLanded",
    "BlueAvgSigStrPct", "BlueAvgSubAtt", "BlueAvgTDLanded", "BlueAvgTDPct",
    "BlueLongestWinStreak", "BlueLosses", "BlueTotalRoundsFought", "BlueTotalTitleBouts",
    "BlueWinsByDecisionMajority", "BlueWinsByDecisionSplit", "BlueWinsByDecisionUnanimous",
    "BlueWinsByKO", "BlueWinsBySubmission", "BlueWinsByTKODoctorStoppage", "BlueWins",
    "BlueStance", "BlueHeightCms", "BlueReachCms", "BlueWeightLbs",
    "RedCurrentLoseStreak", "RedCurrentWinStreak", "RedDraws", "RedAvgSigStrLanded",
    "RedAvgSigStrPct", "RedAvgSubAtt", "RedAvgTDLanded", "RedAvgTDPct",
    "RedLongestWinStreak", "RedLosses", "RedTotalRoundsFought", "RedTotalTitleBouts",
    "RedWinsByDecisionMajority", "RedWinsByDecisionSplit", "RedWinsByDecisionUnanimous",
    "RedWinsByKO", "RedWinsBySubmission", "RedWinsByTKODoctorStoppage", "RedWins",
    "RedStance", "RedHeightCms", "RedReachCms", "RedWeightLbs",
    "BMatchWCRank", "RMatchWCRank",
    "RWFlyweightRank", "RWFeatherweightRank", "RWStrawweightRank", "RWBantamweightRank",
    "RHeavyweightRank", "RLightHeavyweightRank", "RMiddleweightRank", "RWelterweightRank",
    "RLightweightRank", "RFeatherweightRank", "RBantamweightRank", "RFlyweightRank",
    "RPFPRank", "BWFlyweightRank", "BWFeatherweightRank", "BWStrawweightRank",
    "BWBantamweightRank", "BHeavyweightRank", "BLightHeavyweightRank", "BMiddleweightRank",
    "BWelterweightRank", "BLightweightRank", "BFeatherweightRank", "BBantamweightRank",
    "BFlyweightRank", "BPFPRank",
    "Finish", "FinishDetails", "FinishRound", "FinishRoundTime", "TotalFightTimeSecs",
    "RedDecOdds", "BlueDecOdds", "RSubOdds", "BSubOdds", "RKOOdds", "BKOOdds",
    "RedOdds", "BlueOdds", "RedExpectedValue", "BlueExpectedValue", "EmptyArena", "RedFighter", "BlueFighter", "Date", "Location", "Country", "BetterRank"
], axis=1)

"""Foi de 118 colunas para apenas 19"""

df_clean.isna().sum()

"""Das features restantes, nenhuma possui valores faltantes, o que vai ajudar bastante a nossa análise."""

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np

df_clean = df_clean.replace({"Red": -1, "neither": 0, "Blue": 1})
df_clean = df_clean.replace({True: 1, False: 0})
#le = OneHotEncoder()
# Reshape the 'WeightClass' column to be 2D
#weight_class_reshaped = df_clean['WeightClass'].values.reshape(-1, 1)
#df_clean['WeightClass'] = le.fit_transform(weight_class_reshaped).toarray()
df_clean = df_clean.drop("WeightClass", axis=1)
df_clean

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 8))
sns.heatmap(
    df_clean.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    cbar=True
)
plt.title("Mapa de Correlação das Variáveis", fontsize=16)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(data=df, x='AgeDif', kde=True)
plt.title('Distribuição da Diferença de Idade')
plt.show()

sns.scatterplot(data=df, x='AgeDif', y='WinStreakDif', hue='Winner', alpha=0.6)
plt.title('Idade vs. Sequência de Vitórias pelo Resultado')
plt.show()

cols_to_plot = ['Winner', 'AgeDif', 'ReachDif', 'WinStreakDif', 'AvgSubAttDif']
sns.pairplot(df[cols_to_plot], hue='Winner', diag_kind='kde')
plt.show()

y = df_clean["Winner"]
X = df_clean.drop("Winner", axis=1)

import sklearn as skl
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}

grid_search = GridSearchCV(estimator=model, param_grid=param_grid,
                           cv=5, n_jobs=-1, verbose=2, scoring='accuracy')

grid_search.fit(X_train, y_train)

print("Melhores hiperparâmetros:", grid_search.best_params_)

best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia com melhor modelo: {accuracy:.4f}")

"""Melhores hiperparâmetros: {'bootstrap': True, 'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 200}"""

accuracy

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf_model = RandomForestClassifier(
    bootstrap=True,
    max_depth=10,
    min_samples_leaf=1,
    min_samples_split=5,
    n_estimators=200,
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia final: {accuracy:.4f}")

importances = rf_model.feature_importances_

feature_importances = pd.Series(importances, index=X.columns).sort_values(ascending=False)

print("Importância das features:")
print(feature_importances)

from sklearn.neural_network import MLPClassifier

model = MLPClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia final: {accuracy:.4f}")

from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform

param_dist = {
    'hidden_layer_sizes': [(50,), (100,), (50, 50), (100, 50)],
    'activation': ['relu', 'tanh', 'logistic'],
    'solver': ['adam', 'sgd'],
    'alpha': uniform(0.0001, 0.01),
    'learning_rate': ['constant', 'adaptive'],
    'max_iter': [300, 500]
}

random_search = RandomizedSearchCV(model, param_dist, n_iter=20, cv=5, n_jobs=-1, random_state=42, verbose=1)
random_search.fit(X_train, y_train)

print("Melhores hiperparâmetros:")
print(random_search.best_params_)

"""Melhores hiperparâmetros:
{'activation': 'logistic', 'alpha': np.float64(0.004334014807063697), 'hidden_layer_sizes': (50,), 'learning_rate': 'adaptive', 'max_iter': 500, 'solver': 'sgd'}


"""

from sklearn.metrics import accuracy_score

model = MLPClassifier(
        activation='logistic',
        alpha=0.004334014807063697,
        hidden_layer_sizes=(50,),
        learning_rate='adaptive',
        max_iter=500,
        solver='sgd',
        random_state=42
      )

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.4f}")

! pip install shap

import shap
import numpy as np
import pandas as pd

# Garantir subset do X_train
background = shap.sample(X_train, 100, random_state=42)

# Usar apenas probabilidade da classe positiva (1)
explainer = shap.KernelExplainer(lambda x: model.predict_proba(x)[:, 1], background)

# Subamostra de teste
X_test_sample = X_test.iloc[:50] if isinstance(X_test, pd.DataFrame) else X_test[:50]

# SHAP values (agora será um array 2D: (n_amostras, n_features))
shap_values = explainer.shap_values(X_test_sample)

# Feature names
feature_names = (X_train.columns
                 if isinstance(X_train, pd.DataFrame)
                 else [f"f{i}" for i in range(X_train.shape[1])])

# Summary plot (sem erro de shape!)
shap.summary_plot(shap_values, X_test_sample, feature_names=feature_names)

# Force plot individual
shap.initjs()
shap.force_plot(explainer.expected_value,
                shap_values[0],
                X_test_sample.iloc[0] if isinstance(X_test_sample, pd.DataFrame) else X_test_sample[0],
                matplotlib=True)

colunas = [
    "RedLongestWinStreak",
    "RedWins",
    "RedLosses",
    "RedTotalRoundsFought",
    "RedTotalTitleBouts",
    "RedWinsByKO",
    "RedHeightCms",
    "RedReachCms",
    "RedAge",
    "RedAvgSigStrLanded",
    "RedAvgSubAtt",
    "RedAvgTDLanded",
    "RedWinsBySubmission"
]

df[df["RedFighter"] == "Charles Oliveira"][colunas]

df[df["RedFighter"] == "Ilia Topuria"][colunas]

charles = df[df["RedFighter"] == "Charles Oliveira"][colunas].iloc[0]
topuria = df[df["RedFighter"] == "Ilia Topuria"][colunas].iloc[0]

dif = {
    "TitleBout": 1,
    "NumberOfRounds": 5,
    "LoseStreakDif": 0,
    "WinStreakDif": 15,
    "LongestWinStreakDif": topuria["RedLongestWinStreak"] - charles["RedLongestWinStreak"],
    "WinDif": topuria["RedWins"] - charles["RedWins"],
    "LossDif": topuria["RedLosses"] - charles["RedLosses"],
    "TotalRoundDif": topuria["RedTotalRoundsFought"] - charles["RedTotalRoundsFought"],
    "TotalTitleBoutDif": topuria["RedTotalTitleBouts"] - charles["RedTotalTitleBouts"],
    "KODif": topuria["RedWinsByKO"] - charles["RedWinsByKO"] + 1,
    "SubDif": topuria["RedWinsBySubmission"] - charles["RedWinsBySubmission"],
    "HeightDif": topuria["RedHeightCms"] - charles["RedHeightCms"],
    "ReachDif": topuria["RedReachCms"] - charles["RedReachCms"],
    "AgeDif": topuria["RedAge"] - charles["RedAge"],
    "SigStrDif": topuria["RedAvgSigStrLanded"] - charles["RedAvgSigStrLanded"],
    "AvgSubAttDif": topuria["RedAvgSubAtt"] - charles["RedAvgSubAtt"],
    "AvgTDDif": topuria["RedAvgTDLanded"] - charles["RedAvgTDLanded"],
}

novo_df = pd.DataFrame([dif])

novo_df

prediction_Charles_VS_Topuria = rf_model.predict(novo_df)
print(prediction_Charles_VS_Topuria)

colunas = [
    "BlueLongestWinStreak",
    "BlueWins",
    "BlueLosses",
    "BlueTotalRoundsFought",
    "BlueTotalTitleBouts",
    "BlueWinsByKO",
    "BlueHeightCms",
    "BlueReachCms",
    "BlueAge",
    "BlueAvgSigStrLanded",
    "BlueAvgSubAtt",
    "BlueAvgTDLanded",
    "BlueWinsBySubmission",
    "LoseStreakDif",
    "WinStreakDif"
]

df[df["BlueFighter"] == "Max Holloway"][colunas]

df[df["BlueFighter"] == "Dustin Poirier"][colunas]

poirier = df[df["BlueFighter"] == "Dustin Poirier"][colunas].iloc[0]
holloway = df[df["BlueFighter"] == "Max Holloway"][colunas].iloc[0]
dif = {
    "TitleBout": 1,
    "NumberOfRounds": 5,
    "LoseStreakDif": poirier["LoseStreakDif"] - holloway["LoseStreakDif"],
    "WinStreakDif":  poirier["WinStreakDif"] - holloway["WinStreakDif"],
    "LongestWinStreakDif": poirier["BlueLongestWinStreak"] - holloway["BlueLongestWinStreak"],
    "WinDif": poirier["BlueWins"] - holloway["BlueWins"],
    "LossDif": poirier["BlueLosses"] - holloway["BlueLosses"],
    "TotalRoundDif": poirier["BlueTotalRoundsFought"] - holloway["BlueTotalRoundsFought"],
    "TotalTitleBoutDif": poirier["BlueTotalTitleBouts"] - holloway["BlueTotalTitleBouts"],
    "KODif": poirier["BlueWinsByKO"] - holloway["BlueWinsByKO"] + 1,
    "SubDif": poirier["BlueWinsBySubmission"] - holloway["BlueWinsBySubmission"],
    "HeightDif": poirier["BlueHeightCms"] - holloway["BlueHeightCms"],
    "ReachDif": poirier["BlueReachCms"] - holloway["BlueReachCms"],
    "AgeDif": poirier["BlueAge"] - holloway["BlueAge"],
    "SigStrDif": poirier["BlueAvgSigStrLanded"] - holloway["BlueAvgSigStrLanded"],
    "AvgSubAttDif": poirier["BlueAvgSubAtt"] - holloway["BlueAvgSubAtt"],
    "AvgTDDif": poirier["BlueAvgTDLanded"] - holloway["BlueAvgTDLanded"],
}

novo_df = pd.DataFrame([dif])

novo_df

prediction_Holloway_vs_Poirier = rf_model.predict(novo_df)
print(prediction_Holloway_vs_Poirier)