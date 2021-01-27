#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:46:55 2021

@author: @gkuster
"""import pandas as pd
from sklearn.model_selection import train_test_split

base_dados = pd.read_csv('iris.csv')
# Conta ocorrências de um atributo/coluna (neste caso class)
base_dados['class'].value_counts() 

X, _, Y, _ = train_test_split(base_dados.iloc[:, 0:4], base_dados.iloc[:, 4],
                              test_size = 0.5, stratify = base_dados.iloc[:, 4])
# test size pegando 50% dos registros

X.value_counts()
Y.value_counts()


## Infert #####
infert = pd.read_csv('infert.csv')
infert['education'].value_counts()

X1, _, Y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size = 0.6,
                                stratify = infert.iloc[:, 1])
X1.value_counts()
Y1.value_counts()
