import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import fetch_20newsgroups

news = fetch_20newsgroups(subset='all')
print(news.keys()) # type: ignore