import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

loan3000 = pd.read_csv('/content/loan3000.csv')
print(loan3000.head())
loan3000.info()

predictors = ['borrower_score', 'payment_inc_ratio']
outcome = 'outcome'
X = loan3000[predictors]
y = outcome

y = pd.Series([1 if out == 'default' else 0 for out in loan3000['outcome']])

from xgboost import XGBClassifier

xgb = XGBClassifier(objective='binary:logistic', subsmaple=0.63, eval_metric='error')

xgb.fit(X, y)


xgb_df= X.copy()
xgb_df['prediction'] = ['default' if out == 1 else 'paid off' for out in xgb.predict(X)]
xgb_df['prob_default'] = xgb.predict_proba(X)[:,0]
xgb_df.head()
from sklearn.metrics import accuracy_score

accuracy_score(y, xgb.predict(X))

fig, ax = plt.subplots(figsize=(10, 10))
xgb_df.loc[xgb_df.prediction == 'paid off'].plot(x='borrower_score', y='payment_inc_ratio', style='.', markerfacecolor='none', markeredgecolor='C1', ax=ax)
xgb_df.loc[xgb_df.prediction == 'default'].plot(x='borrower_score', y='payment_inc_ratio', style='o', markerfacecolor='none', markeredgecolor='C0', ax=ax)
ax.legend(['paid off', 'default'])


