#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 22:41:55 2021

@author: @gkuster
"""

import numpy as np
import pandas as pd
from math import ceil # Usado para arredondamento de cálculos

populacao = 150
amostra = 15
k = ceil(populacao / amostra)

r = np.random.randint(low = 1, high = k+1, size = 1)

acumulador = r[0]
sorteados = []

for i in range (amostra):
    sorteados.append(acumulador)
    acumulador += k

# Carrega a base iris.csv e retorna os valores de acordo com o sorteio
base = pd.read_csv('iris.csv')
base_final = base.loc[sorteados]
