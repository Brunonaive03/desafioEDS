import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

# datas de entrada
datas_atendimentos = []

# converter para datetime
datas_atendimentos = [datetime.strptime(data, "%Y-%m-%d") for data in datas_atendimentos]

# contar a quantidade de atendimentos por dia
contagem_atendimentos = Counter(datas_atendimentos)

# separar as datas e as contagens
datas = list(contagem_atendimentos.keys())
contagens = list(contagem_atendimentos.values())


plt.figure(figsize=(10, 6))
plt.bar(datas, contagens, color='blue')
plt.xlabel('Data')
plt.ylabel('Quantidade')
plt.title('Atendimentos Médicos por Dia')
plt.xticks(datas, rotation=45, ha='right')  # ajustar o espaçamento entre os ticks
plt.tight_layout()


plt.show()
