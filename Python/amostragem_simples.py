#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:34:09 2021

@author: @gkuster
"""

import pandas as pd
import numpy as np

base_dados = pd.read_csv('iris.csv')
base_dados.shape

np.random.seed(888) # Repete amostras para repetição de testes
amostra = np.random.choice(a = [0,1], size = 150, replace=True, p=[0.5,0.5])
amostra.shape

len(amostra)
len(amostra[amostra==1]) # Retorna o total de elementos informados
len(amostra[amostra==0]) # Retorna o total de elementos informados

