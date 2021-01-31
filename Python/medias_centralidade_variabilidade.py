#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @date: Jan/21   @author: @gkuster

import numpy as np
from scipy import stats

jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]

# Média
media = np.mean(jogadores)
media

# Mediana
mediana = np.median(jogadores)
mediana

# Quartis
quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1])
quartis

# Desvio padrão
desvio1 = np.std(jogadores)
desvio1

desvio2 = np.std(jogadores, ddof = 1)
desvio2

# Resumo da variável
stats.describe(jogadores)