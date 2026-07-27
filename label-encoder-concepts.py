#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 00:03:20 2026

@author: sachinshelke
"""
import numpy as np
np.__version__


from sklearn.preprocessing import LabelEncoder

# Sample categorical data
colors = ["Red", "Blue", "Green", "Blue", "Red"]

# create label encoder
encoder = LabelEncoder()

#Fit and Transfrom the data
encoder_colors = encoder.fit(colors)

encoder_colors = encoder.transform(colors)

print(encoder_colors)

