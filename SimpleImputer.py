#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 00:20:44 2026

@author: sachinshelke
"""

import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer

df = pd.DataFrame(
    {
     "Age": [25,20, None, 35,40],
     "Salary":[5000, 4000, np.nan, 1000,2000]
     }
    )

imputer = SimpleImputer(strategy="mean")

imputer.fit(df[["Age", "Salary"]])

df[["Age", "Salary"]] = imputer.transform(df[["Age", "Salary"]])

print(df)