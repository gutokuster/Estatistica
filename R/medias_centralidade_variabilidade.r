# Salários 
jogadores = c(40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000)

# Media
mean(jogadores)

# Mediana
median(jogadores)

# Quartis
quartis = quantile(jogadores)
quartis

# Por posição
quartis[0]
quartis[1]
quartis[2]
quartis[3]
quartis[4]

# Desvio padrão - Standart Desviation
sd(jogadores)

# Resumo da variável
summary(jogadores)