#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:08:32 2026

@author: sachinshelke
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"./Practice-data-sets/Data.csv")

#Independent variable

X = dataset.iloc[:,:-1].values

