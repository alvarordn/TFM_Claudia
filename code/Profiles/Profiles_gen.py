import json
import numpy as np
import matplotlib.pyplot as plt
import copy

# Leo el json de data
with open('data.json', 'r') as file:
    data = json.load(file)

# Asigno datos cada cinco minutos 288 datos  
indices = list(np.linspace(0, len(data['Demanda']) - 1, 288, dtype=int))
Demanda = [data['Demanda'][i]/1e5 for i in indices]
Eolica = [data['Eolica'][i]/1e5 for i in indices]
PV = [data['PV'][i]/1e5 for i in indices]

# Dibujo los perfiles
x_horas = np.arange(288) * (5 / 60)  # 5 minutos -> horas
fig, axs = plt.subplots(3, 1, figsize=(8, 8), sharex=True)

axs[0].plot(x_horas, PV, label='PV', color='gold')
axs[0].set_ylabel('PV')
axs[0].grid(True)

axs[1].plot(x_horas, Demanda, label='Demanda', color='blue')
axs[1].set_ylabel('Demanda')
axs[1].grid(True)

axs[2].plot(x_horas, Eolica, label='Eólica', color='green')
axs[2].set_ylabel('Eólica')
axs[2].set_xlabel('Tiempo (h)')
axs[2].grid(True)

plt.xlim(0, 24)

xticks = np.arange(0, 25, 2)
for ax in axs:
    ax.set_xticks(xticks)

# Leo el mat de EV
with open('EV.json', 'r') as file:
    data = json.load(file)
    
# Tomo los datos (son minutos)
EV1 = data['P_EV'][0][::5]
EV2 = data['P_EV'][1][::5]

# Genero un vector de 288 componentes de ceros
EV_base = list(np.zeros(288))

# Tomo un número random entre 0 y 288 - 7 y pongo el perfil de carga
EV = list()
for _ in range(20):
    if np.random.rand() < 0.5:
        EV_aux = copy.copy(EV_base)
        rnd_num = np.random.randint(0, 288-7)
        EV_aux[rnd_num : rnd_num + 7] = EV1
        EV.append(EV_aux)
    else:
        EV_aux = copy.copy(EV_base)
        rnd_num = np.random.randint(0, 288-7)
        EV_aux[rnd_num : rnd_num + 7] = EV2
        EV.append(EV_aux)
    
    
# Guardo los perfiles
data = {'Demanda': Demanda, 
        'Eolica': Eolica,
        'PV': PV,
        'EV': EV}
with open('Claudia.json', 'w') as fp:
	json.dump(data, fp, indent=4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
