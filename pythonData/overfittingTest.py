# colab 실행

# 1
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 2
folder = "/content/"
loan_data = pd.read_csv(folder + "loan_data.csv.gz")
print(loan_data.head())
print(loan_data.info())

# 3
predictors = ["loan_amnt", "term", "annual_inc", "dti", "payment_inc_ratio", "revol_bal", "revol_util", "purpose", "delinq_2yrs_zero", "pub_rec_zero", "open_acc", "grade", "emp_length", "purpose_", "home_", "emp_len_", "borrower_score"]
outcome = 'outcome'

X = pd.get_dummies(loan_data[predictors], drop_first=True, dtype=int)
y = pd.Series([1 if out =='default' else 0 for out in loan_data[outcome]])

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=10000)

# 4
from xgboost import XGBClassifier

xgb_default = XGBClassifier(objective='binary:logistic', n_estimators=250,
                            max_depth=6, reg_lambda=0, learning_rate=0.3, subsample=1)
xgb_default.fit(train_X, train_y)
pred_default = xgb_default.predict(test_X)
error_default = abs(test_y - pred_default) > 0.5
print(f"error_default mean : {np.mean(error_default)}")
print(f"acc : {accuracy_score(test_y, pred_default)}")

# 5
predictors = ["loan_amnt", "term", "annual_inc", "dti", "payment_inc_ratio", "revol_bal", "revol_util", "purpose", "delinq_2yrs_zero", "pub_rec_zero", "open_acc", "grade", "emp_length", "purpose_", "home_", "emp_len_", "borrower_score"]
outcome = 'outcome'

X = pd.get_dummies(loan_data[predictors], drop_first=True, dtype=int)
y = pd.Series([1 if out =='default' else 0 for out in loan_data[outcome]])

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=10000)

from xgboost import XGBClassifier

xgb_panalty = XGBClassifier(objective='binary:logistic', n_estimators=250,
                            max_depth=6, reg_lambda=1000, learning_rate=0.3, subsample=1)
xgb_panalty.fit(train_X, train_y)
pred_default = xgb_panalty.predict(test_X)
error_default = abs(test_y - pred_default) > 0.5
print(f"error_default mean : {np.mean(error_default)}")
print(f"acc : {accuracy_score(test_y, pred_default)}")

# 6
results = []
for ntree_limit in range(1, 250):
  iteration_range = [1, ntree_limit + 1]
  train_default = xgb_default.predict_proba(train_X, iteration_range=iteration_range)[:, 1]
  train_panalty = xgb_panalty.predict_proba(train_X, iteration_range=iteration_range)[:, 1]
  pred_default = xgb_default.predict_proba(test_X, iteration_range=iteration_range)[:, 1]
  pred_panalty = xgb_panalty.predict_proba(test_X, iteration_range=iteration_range)[:, 1]
  results.append({
      'iterations' : ntree_limit,
      'default train' : np.mean(abs(train_y - train_default) > 0.5),
      'panalty train' : np.mean(abs(train_y - train_panalty) > 0.5),
      'default test' : np.mean(abs(test_y - pred_default) > 0.5),
      'panalty test' : np.mean(abs(test_y - pred_panalty) > 0.5)
  })
results = pd.DataFrame(results)
results.head()

# 7 
fig = plt.figure()
ax = fig.add_subplot()
results.plot(x='iterations', y='default test', ax=ax)
results.plot(x='iterations', y='panalty test', ax=ax)
results.plot(x='iterations', y='default train', ax=ax)
results.plot(x='iterations', y='panalty train', ax=ax)
plt.show()