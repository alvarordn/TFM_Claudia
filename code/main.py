# Importing required libraries
import numpy as np
import lib
import matplotlib.pyplot as plt
import os
#en desiquilibrado no trabajamos en por unidad

Ubase = 400 #V
#Zbase = (Ubase**2)/Sbase
import json
with open('Claudia.json', 'r') as file:
    data = json.load(file)
pv_pu = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.053762360055569176, 0.05425518918035452, 0.07163861649096995, 0.09046888761769863, 0.11860897732741302, 0.15425444689602538, 0.1827898994851679, 0.1827898994851679, 0.1827898994851679, 0.221008133347861, 0.2911586672477823, 0.35116025623564173, 0.44287090381629424, 0.5082795006946145, 0.5915660156356398, 0.6504106852623638, 0.7042356400897093, 0.7631169926361762, 0.8116373838903868, 0.839518128081501, 0.873323277310161, 0.9109644702314473, 0.9457492304758787, 0.9751181525973139, 0.9818211843861513, 0.9815211843861513, 0.9878211843861513, 0.9818211843861513, 0.9878211843861513, 0.9888211843861513, 0.9898211843861513, 0.9928211843861513, 0.9938211843861513, 0.9948211843861513, 0.9958211843861513, 0.9988211843861513, 0.9998211843861513, 1, 1, 1, 1, 1, 1, 1, 0.9998211843861513, 1, 1, 0.9995211843861513, 0.9898211843861513, 0.9998211843861513, 1, 1, 1, 0.9998211843861513, 0.9998211843861513, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.9998211843861513, 0.9988211843861513, 0.9878211843861513, 0.9768211843861513, 0.9658211843861513, 0.9548211843861513, 0.920535261910599, 0.9198211843861513, 0.9088211843861513, 0.8978211843861513, 0.8568211843861513, 0.8358211843861513, 0.8248211843861513, 0.788646250442646, 0.7796323990084715, 0.7567720846612732, 0.7045149955054343, 0.6845149955054343, 0.6596589771004124, 0.608211843861513, 0.5558211843861513, 0.5848211843861513, 0.548646250442646, 0.5296323990084715, 0.4067720846612732, 0.3245149955054343, 0.2545149955054343, 0.2445149955054343, 0.2245149955054343, 0.2045149955054343, 0.1845149955054343, 0.15451499550543432, 0.11060897732741302, 0.11160897732741302, 0.11060897732741302, 0.10960897732741302, 0.10860897732741302, 0.1103608977327413, 0.09046888761769863, 0.0716, 0.0686, 0.0656, 0.0626, 0.0596, 0.0566, 0.0536, 0.03, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


# Crear vector de tiempo en horas (cada 5 minutos = 1/12 h)
tiempo = np.arange(0, 24, 5/60)  # 288 puntos de 5 minutos en 24 horas

# Crear la figura
plt.figure(figsize=(12, 6))

# Graficar las series
plt.plot(tiempo, data['Demanda'], label='Demanda')
plt.plot(tiempo, pv_pu, label='PV')
linestyles = ['-', '--', '-.', ':']
for i in range(19):
    estilo = linestyles[i % len(linestyles)]
    plt.plot(tiempo, data['EV'][i], linestyle=estilo, label=f'EV_{i+1}')

# Etiquetas y estilo
plt.xlabel('Hora del día')
plt.ylabel('PERFILES (pu)')
plt.title('DATA.JSON')
plt.xlim(0, 24)
plt.ylim(0, 1)
plt.xticks(np.arange(0, 25, 1))  # marcas horarias cada hora
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()

L_a=0.035 #km
L_b=0.03 #km
L_c=0.2 #km

Z_pOH1 = np.array([
    [0.540 + 0.777j, 0.049 + 0.505j, 0.049 + 0.462j, 0.049 + 0.436j],
    [0.049 + 0.505j, 0.540 + 0.777j, 0.049 + 0.505j, 0.049 + 0.462j],
    [0.049 + 0.462j, 0.049 + 0.505j, 0.540 + 0.777j, 0.049 + 0.505j],
    [0.049 + 0.436j, 0.049 + 0.462j, 0.049 + 0.505j, 0.540 + 0.777j]])

Z_pOH2 = np.array([
    [1.369 + 0.812j, 0.049 + 0.505j, 0.049 + 0.462j, 0.049 + 0.436j],
    [0.049 + 0.505j, 1.369 + 0.812j, 0.049 + 0.505j, 0.049 + 0.462j],
    [0.049 + 0.462j, 0.049 + 0.505j, 1.369 + 0.812j, 0.049 + 0.505j],
    [0.049 + 0.436j, 0.049 + 0.462j, 0.049 + 0.505j, 1.369 + 0.812j]])

Z_pOH3 = np.array([
    [2.065 + 0.825j, 0.049 + 0.505j, 0.049 + 0.462j, 0.049 + 0.436j],
    [0.049 + 0.505j, 2.065 + 0.825j, 0.049 + 0.505j, 0.049 + 0.462j],
    [0.049 + 0.462j, 0.049 + 0.505j, 2.065 + 0.825j, 0.049 + 0.505j],
    [0.049 + 0.436j, 0.049 + 0.462j, 0.049 + 0.505j, 2.065 + 0.825j]])
    
Z_pUG1 = np.array([
    [0.211 + 0.747j, 0.049 + 0.673j, 0.049 + 0.651j, 0.049 + 0.673j],
    [0.049 + 0.673j, 0.211 + 0.747j, 0.049 + 0.673j, 0.049 + 0.651j],
    [0.049 + 0.651j, 0.049 + 0.673j, 0.211 + 0.747j, 0.049 + 0.673j],
    [0.049 + 0.673j, 0.049 + 0.651j, 0.049 + 0.673j, 0.211 + 0.747j]])
    
Z_pUG2 = np.array([
    [0.314 + 0.762j, 0.049 + 0.687j, 0.049 + 0.665j, 0.049 + 0.687j],
    [0.049 + 0.687j, 0.314 + 0.762j, 0.049 + 0.687j, 0.049 + 0.665j],
    [0.049 + 0.665j, 0.049 + 0.687j, 0.314 + 0.762j, 0.049 + 0.687j],
    [0.049 + 0.687j, 0.049 + 0.665j, 0.049 + 0.687j, 0.314 + 0.762j]])

Z_pUG3 = np.array([
    [0.871 + 0.797j, 0.049 + 0.719j, 0.049 + 0.697j, 0.049 + 0.719j],
    [0.049 + 0.719j, 0.871 + 0.797j, 0.049 + 0.719j, 0.049 + 0.697j],
    [0.049 + 0.697j, 0.049 + 0.719j, 0.871 + 0.797j, 0.049 + 0.719j],
    [0.049 + 0.719j, 0.049 + 0.697j, 0.049 + 0.719j, 0.871 + 0.797j]])
    


S_HOUSE_PV=10000 #VA
S_BLOCK_PV= 30000
S_MARKET_PV=60000
S_INDUSTRY_PV=100000


S_HOUSE_D=7000 #VA
S_BLOCK_D= 50000
S_MARKET_D=90000
S_INDUSTRY_D=90000

S_EV= 7000


fdp_EV = 1
fdp_PV = 1
fdp_D = 0.95




# Nodes
Nodes = [
    {'id': 'X1', 'slack': True},
    {'id': 'R2', 'slack': False},
    {'id': 'R3', 'slack': False},
    {'id': 'R4', 'slack': False},
    {'id': 'R5', 'slack': False},
    {'id': 'R6', 'slack': False},
    {'id': 'R7', 'slack': False},
    {'id': 'R8', 'slack': False},
    {'id': 'R9', 'slack': False},
    {'id': 'R10', 'slack': False},
    {'id': 'R11', 'slack': False},
    {'id': 'R12', 'slack': False},
    {'id': 'R13', 'slack': False},
    {'id': 'R14', 'slack': False},
    {'id': 'R15', 'slack': False},
    {'id': 'R16', 'slack': False},
    {'id': 'R17', 'slack': False},
    {'id': 'R18', 'slack': False},
    {'id': 'I2', 'slack': False},
    {'id': 'C2', 'slack': False},
    {'id': 'C3', 'slack': False},
    {'id': 'C4', 'slack': False},
    {'id': 'C5', 'slack': False},
    {'id': 'C6', 'slack': False},
    {'id': 'C7', 'slack': False},
    {'id': 'C8', 'slack': False},
    {'id': 'C9', 'slack': False},
    {'id': 'C10', 'slack': False},
    {'id': 'C11', 'slack': False},
    {'id': 'C12', 'slack': False},
    {'id': 'C13', 'slack': False},
    {'id': 'C14', 'slack': False},
    {'id': 'C15', 'slack': False},
    {'id': 'C16', 'slack': False},
    {'id': 'C17', 'slack': False},
    {'id': 'C18', 'slack': False},
    {'id': 'C19', 'slack': False},
    {'id': 'C20', 'slack': False}
]
#CURVA PATO
DUCK_CURVE=[]

for i in range(288): 
    DUCK_CURVE.append(data['Demanda'][i]-pv_pu[i])
    
# Crear vector de tiempo en horas (cada 5 minutos = 1/12 h)
tiempo = np.arange(0, 24, 5/60)  # 288 puntos de 5 minutos en 24 horas

# Crear la figura
plt.figure(figsize=(12, 6))

# Graficar las series
plt.plot(tiempo, np.array(data['Demanda'])/1000, label='Demanda', alpha=0.5)
plt.plot(tiempo, np.array(DUCK_CURVE)/1000, label='Demanda cubierta por FV')
plt.plot(tiempo, np.array(pv_pu)/1000, label='PV', alpha=0.5)

# Etiquetas y estilo
plt.xlabel('Hora del día')
plt.ylabel('Potencia en kW')
plt.title('CURVA PATO')
plt.xlim(0, 24)
plt.xticks(np.arange(0, 25, 1))  # marcas horarias cada hora
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()


# Lines
Lines = [
    {'id': 0, 'From': 'X1', 'To': 'R2', 'Z_p': Z_pUG1 * L_a},
    {'id': 1, 'From': 'R2', 'To': 'R3', 'Z_p': Z_pUG1 * L_a},
    {'id': 2, 'From': 'R3', 'To': 'R4', 'Z_p': Z_pUG1 * L_a},
    {'id': 3, 'From': 'R4', 'To': 'R5', 'Z_p': Z_pUG1 * L_a},
    {'id': 4, 'From': 'R5', 'To': 'R6', 'Z_p': Z_pUG1 * L_a},
    {'id': 5, 'From': 'R6', 'To': 'R7', 'Z_p': Z_pUG1 * L_a},
    {'id': 6, 'From': 'R7', 'To': 'R8', 'Z_p': Z_pUG1 * L_a},
    {'id': 7, 'From': 'R8', 'To': 'R9', 'Z_p': Z_pUG1 * L_a},
    {'id': 8, 'From': 'R9', 'To': 'R10', 'Z_p': Z_pUG1 * L_a},
    {'id': 9, 'From': 'R3', 'To': 'R11', 'Z_p': Z_pUG1 * L_a},
    {'id': 10, 'From': 'R4', 'To': 'R12', 'Z_p': Z_pUG1 * L_a},
    {'id': 11, 'From': 'R12', 'To': 'R13', 'Z_p': Z_pUG1 * L_a},
    {'id': 12, 'From': 'R13', 'To': 'R14', 'Z_p': Z_pUG1 * L_a},
    {'id': 13, 'From': 'R14', 'To': 'R15', 'Z_p': Z_pUG1 * L_a},
    {'id': 14, 'From': 'R6', 'To': 'R16', 'Z_p': Z_pUG1 * L_a},
    {'id': 15, 'From': 'R9', 'To': 'R17', 'Z_p': Z_pUG1 * L_a},
    {'id': 16, 'From': 'R10', 'To': 'R18', 'Z_p': Z_pUG1 * L_a},
    {'id': 17, 'From': 'X1', 'To': 'I2', 'Z_p': Z_pUG2 * L_c},
    {'id': 18, 'From': 'X1', 'To': 'C2', 'Z_p': Z_pOH1 * L_b},
    {'id': 19, 'From': 'C2', 'To': 'C3', 'Z_p': Z_pOH1 * L_b},
    {'id': 20, 'From': 'C3', 'To': 'C4', 'Z_p': Z_pOH1 * L_b},
    {'id': 21, 'From': 'C4', 'To': 'C5', 'Z_p': Z_pOH1 * L_b},
    {'id': 22, 'From': 'C5', 'To': 'C6', 'Z_p': Z_pOH1 * L_b},
    {'id': 23, 'From': 'C6', 'To': 'C7', 'Z_p': Z_pOH1 * L_b},
    {'id': 24, 'From': 'C7', 'To': 'C8', 'Z_p': Z_pOH1 * L_b},
    {'id': 25, 'From': 'C8', 'To': 'C9', 'Z_p': Z_pOH1 * L_b},
    {'id': 26, 'From': 'C3', 'To': 'C10', 'Z_p': Z_pOH2 * L_b},
    {'id': 27, 'From': 'C10', 'To': 'C11', 'Z_p': Z_pOH2 * L_b},
    {'id': 28, 'From': 'C11', 'To': 'C12', 'Z_p': Z_pOH2 * L_b},
    {'id': 29, 'From': 'C11', 'To': 'C13', 'Z_p': Z_pOH2 * L_b},
    {'id': 30, 'From': 'C10', 'To': 'C14', 'Z_p': Z_pOH2 * L_b},
    {'id': 31, 'From': 'C5', 'To': 'C15', 'Z_p': Z_pOH2 * L_b},
    {'id': 32, 'From': 'C15', 'To': 'C16', 'Z_p': Z_pOH2 * L_b},
    {'id': 33, 'From': 'C15', 'To': 'C17', 'Z_p': Z_pOH3 * L_b},
    {'id': 34, 'From': 'C16', 'To': 'C18', 'Z_p': Z_pOH3 * L_b},
    {'id': 35, 'From': 'C8', 'To': 'C19', 'Z_p': Z_pOH3 * L_b},
    {'id': 36, 'From': 'C9', 'To': 'C20', 'Z_p': Z_pOH3 * L_b}
]
# Prosumers
KPI_U=[]
P_head=[]

for p in range(288):
    # Prosumers
    Pros = [
        {'id': "V1",  'Node': 'R2',  'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3), 'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "V2",  'Node': 'R3',  'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "V3",  'Node': 'R4',  'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "V4",  'Node': 'R5',  'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "V5",  'Node': 'R6',  'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "V6",  'Node': 'R7',  'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "V7",  'Node': 'R8',  'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "V8",  'Node': 'R9',  'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "V9",  'Node': 'R10', 'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "V10", 'Node': 'R11', 'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "B1", 'Node': 'R12', 'P': -np.array([(S_BLOCK_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_BLOCK_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "B2", 'Node': 'R13', 'P': -np.array([(S_BLOCK_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_BLOCK_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "B3", 'Node': 'R14', 'P': -np.array([(S_BLOCK_D*data['Demanda'][p]*fdp_D)/3]*3), 'Q': -np.array([(S_BLOCK_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "B4", 'Node': 'R15', 'P': -np.array([(S_BLOCK_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_BLOCK_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "B5", 'Node': 'R16', 'P': -np.array([(S_BLOCK_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_BLOCK_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "B6", 'Node': 'R17', 'P': -np.array([(S_BLOCK_D*data['Demanda'][p]*fdp_D)/3]*3), 'Q': -np.array([(S_BLOCK_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "B7", 'Node': 'R18', 'P': -np.array([(S_BLOCK_D*data['Demanda'][p]*fdp_D)/3]*3), 'Q': -np.array([(S_BLOCK_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "MARKET", 'Node': 'C2', 'P': -np.array([(S_MARKET_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_MARKET_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "S1",  'Node': 'C9',  'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "S2",  'Node': 'C10',  'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "S3",  'Node': 'C11',  'P': -np.array([(S_HOUSE_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_HOUSE_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "IND", 'Node': 'I2', 'P': -np.array([(S_INDUSTRY_D*data['Demanda'][p]*fdp_D)/3]*3),  'Q': -np.array([(S_INDUSTRY_D*data['Demanda'][p]*np.sin(np.arccos(fdp_D)))/3]*3)},
        {'id': "V1_PV",  'Node': 'R2', 'P': np.array([(S_HOUSE_PV*pv_pu[p]*fdp_PV)/3]*3), 'Q': np.array([(S_HOUSE_PV*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "V2_PV",  'Node': 'R3',  'P': np.array([(S_HOUSE_PV*pv_pu[p]*fdp_PV)/3]*3), 'Q': np.array([(S_HOUSE_PV*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "V3_PV",  'Node': 'R4',  'P': np.array([(S_HOUSE_PV*pv_pu[p]*fdp_PV)/3]*3), 'Q': np.array([(S_HOUSE_PV*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "V4_PV",  'Node': 'R5',  'P': np.array([(S_HOUSE_PV*pv_pu[p]*fdp_PV)/3]*3), 'Q': np.array([(S_HOUSE_PV*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "V5_PV",  'Node': 'R6',  'P': np.array([(S_HOUSE_PV*pv_pu[p]*fdp_PV)/3]*3), 'Q': np.array([(S_HOUSE_PV*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "V6_PV",  'Node': 'R7',  'P': np.array([(S_HOUSE_PV*pv_pu[p]*fdp_PV)/3]*3), 'Q': np.array([(S_HOUSE_PV*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "V7_PV",  'Node': 'R8',  'P': np.array([(S_HOUSE_PV*pv_pu[p]*fdp_PV)/3]*3), 'Q': np.array([(S_HOUSE_PV*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "B2_PV", 'Node': 'R12', 'P': np.array([(S_BLOCK_PV*pv_pu[p]*fdp_PV)/3]*3),  'Q': np.array([(S_BLOCK_D*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "B3_PV", 'Node': 'R13', 'P': np.array([(S_BLOCK_PV*pv_pu[p]*fdp_PV)/3]*3),  'Q': np.array([(S_BLOCK_D*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "B4_PV", 'Node': 'R14', 'P': np.array([(S_BLOCK_PV*pv_pu[p]*fdp_PV)/3]*3),  'Q': np.array([(S_BLOCK_D*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "B5_PV", 'Node': 'R15', 'P': np.array([(S_BLOCK_PV*pv_pu[p]*fdp_PV)/3]*3),  'Q': np.array([(S_BLOCK_D*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "B6_PV", 'Node': 'R16', 'P': np.array([(S_BLOCK_PV*pv_pu[p]*fdp_PV)/3]*3),  'Q': np.array([(S_BLOCK_D*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "S1_PV",  'Node': 'C9',  'P': np.array([(S_HOUSE_PV*pv_pu[p]*fdp_PV)/3]*3), 'Q': np.array([(S_HOUSE_PV*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "S3_PV",  'Node': 'C11',  'P': np.array([(S_HOUSE_PV*pv_pu[p]*fdp_PV)/3]*3), 'Q': np.array([(S_HOUSE_PV*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "MARKET_PV", 'Node': 'C16', 'P': -np.array([(S_MARKET_PV*pv_pu[p]*fdp_PV)/3]*3),  'Q': np.array([(S_MARKET_PV*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        {'id': "IND_PV", 'Node': 'I2', 'P': np.array([(S_INDUSTRY_PV*pv_pu[p]*fdp_PV)/3]*3),  'Q': -np.array([(S_INDUSTRY_PV*pv_pu[p]*np.sin(np.arccos(fdp_PV)))/3]*3)},
        # {'id': "C6_EV", 'Node': 'C6', 'P': -np.array([(S_EV*data['EV'][1][p]*fdp_EV)/3]*3),  'Q': -np.array([(S_EV*data['EV'][1][p]*np.sin(np.arccos(fdp_EV)))/3]*3)},
        # {'id': "C7_EV", 'Node': 'C7', 'P': -np.array([(S_EV*data['EV'][2][p]*fdp_EV)/3]*3),  'Q': -np.array([(S_EV*data['EV'][2][p]*np.sin(np.arccos(fdp_EV)))/3]*3)},
        # {'id': "C8_EV", 'Node': 'C8', 'P': -np.array([(S_EV*data['EV'][3][p]*fdp_EV)/3]*3),  'Q': -np.array([(S_EV*data['EV'][3][p]*np.sin(np.arccos(fdp_EV)))/3]*3)},
        # {'id': "V2_EV", 'Node': 'R3', 'P': -np.array([(S_EV * data['EV'][4][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][4][p] * np.sin(np.arccos(fdp_EV)))/3] * 3)},
        # {'id': "V3_EV", 'Node': 'R4', 'P': -np.array([(S_EV * data['EV'][5][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][5][p] * np.sin(np.arccos(fdp_EV)))/3] * 3)},
        # {'id': "V4_EV", 'Node': 'R5', 'P': -np.array([(S_EV * data['EV'][6][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][6][p] * np.sin(np.arccos(fdp_EV)))/3] * 3)},
        # {'id': "V5_EV", 'Node': 'R6', 'P': -np.array([(S_EV * data['EV'][7][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][7][p] * np.sin(np.arccos(fdp_EV)))/3] * 3)},
        # {'id': "V6_EV", 'Node': 'R7', 'P': -np.array([(S_EV * data['EV'][8][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][8][p] * np.sin(np.arccos(fdp_EV)))/3] * 3)},
        # {'id': "V7_EV", 'Node': 'R8', 'P': -np.array([(S_EV * data['EV'][9][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][9][p] * np.sin(np.arccos(fdp_EV)))/3] * 3)},
        # {'id': "V8_EV", 'Node': 'R9', 'P': -np.array([(S_EV * data['EV'][10][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][10][p] * np.sin(np.arccos(fdp_EV))) / 3] * 3)},
        # {'id': "V8_EV", 'Node': 'R9', 'P': -np.array([(S_EV * data['EV'][10][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][10][p] * np.sin(np.arccos(fdp_EV))) / 3] * 3)},
        # {'id': "B1_EV", 'Node': 'R12', 'P': -np.array([(S_EV * data['EV'][11][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][11][p] * np.sin(np.arccos(fdp_EV))) / 3] * 3)},
        # {'id': "B2_EV", 'Node': 'R13', 'P': -np.array([(S_EV * data['EV'][12][p] * fdp_EV) / 3] * 3), 'Q': -np.array([(S_EV * data['EV'][12][p] * np.sin(np.arccos(fdp_EV))) / 3] * 3)},
        # {'id': "B3_EV", 'Node': 'R14', 'P': -np.array([(S_EV * data['EV'][13][p] * fdp_EV) / 3] * 3), 'Q': -np.array([(S_EV * data['EV'][13][p] * np.sin(np.arccos(fdp_EV))) / 3] * 3)},
        # {'id': "B4_EV", 'Node': 'R15', 'P': -np.array([(S_EV * data['EV'][14][p] * fdp_EV) / 3] * 3), 'Q': -np.array([(S_EV * data['EV'][14][p] * np.sin(np.arccos(fdp_EV))) / 3] * 3)},
        # {'id': "B5_EV", 'Node': 'R16', 'P': -np.array([(S_EV * data['EV'][15][p] * fdp_EV) / 3] * 3), 'Q': -np.array([(S_EV * data['EV'][15][p] * np.sin(np.arccos(fdp_EV))) / 3] * 3)},
        # {'id': "B6_EV", 'Node': 'R17', 'P': -np.array([(S_EV * data['EV'][16][p] * fdp_EV) / 3] * 3), 'Q': -np.array([(S_EV * data['EV'][16][p] * np.sin(np.arccos(fdp_EV))) / 3] * 3)},
        # {'id': "S1_EV", 'Node': 'C9', 'P': -np.array([(S_EV * data['EV'][17][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][17][p] * np.sin(np.arccos(fdp_EV)))/3] * 3)},
        # {'id': "S2_EV", 'Node': 'C10', 'P': -np.array([(S_EV * data['EV'][18][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][18][p] * np.sin(np.arccos(fdp_EV)))/3] * 3)},
        # {'id': "S3_EV", 'Node': 'C11', 'P': -np.array([(S_EV * data['EV'][19][p] * fdp_EV) / 3]*3), 'Q': -np.array([(S_EV * data['EV'][19][p] * np.sin(np.arccos(fdp_EV)))/3] * 3)},
        ]
    net = lib.grid(Nodes, Lines, Pros)


    #sol, infodict, ier, mesg = net.solve_pf()

    sol, _, _, _ = net.solve_pf()  # Ignora infodict, ier y mesg
    
    # 0, 17, 18
    I_head = net.lines[0].I + net.lines[17].I + net.lines[18].I    
    S_temp = (net.nodes[0].U[0]-net.nodes[0].U[3])*np.conj(I_head[0])+(net.nodes[0].U[1]-net.nodes[0].U[3])*np.conj(I_head[1])+(net.nodes[0].U[2]-net.nodes[0].U[3])*np.conj(I_head[2])
    
    P_head.append(abs(S_temp.real))
    
    #KPI TENSIÓN 10% (POR FASES)
    for q in range(len(net.nodes)):
            for i in range(len(net.nodes[q].U)-1):
                if abs(net.nodes[q].U[i]-net.nodes[q].U[3])>=(1.1*400/np.sqrt(3)):
                    KPI_U.append([{'id': net.nodes[q].ref, 'U':(net.nodes[q].U[i]-net.nodes[q].U[3]), '+%':(net.nodes[q].U[i]/(400/np.sqrt(3))*100-100),'Time': p}])
                else:
                    if abs(net.nodes[q].U[i]-net.nodes[q].U[3])<=0.9*400/np.sqrt(3):
                        KPI_U.append([{'id': net.nodes[q].ref, 'U':(net.nodes[q].U[i]-net.nodes[q].U[3]), '-%':(100-net.nodes[q].U[i]/(400/np.sqrt(3))*100), 'Time': p}])

#grafica de cabecera
tiempo = np.arange(0, 24, 5/60) 
plt.figure(figsize=(12, 6))
plt.plot(tiempo, P_head, label='Potencia', color='tab:blue')

# Etiquetas
plt.xlabel('Hora del día')
plt.ylabel('Potencia [W]') 
plt.title('Evolución de la potencia en cabecera')
plt.show()


# tension_temp=[]
# for q in range(len(net.nodes)):
#     for i in range(len(net.nodes[q].U)-1):
#         tension_temp.append(abs(net.nodes[q].U[i]-net.nodes[q].U[3]))


# Algunos comandos interesantes
# net.__dict__
# 
# net.nodes[0].lines[0].__dict__
# net.nodes[0].lines[0].nodes[0].__dict__

# for node in net.nodes:
#     print(node.__dict__)

# print(net.pros[1].Iang)
# print(net.pros[1].Imagn)
# print(net.lines[12].Imag)
# print(net.lines[12].Iang)
# print(net.nodes[14].Uang)
# print(net.nodes[14].Umag)
# print(net.lines[12].S_in)
# print(net.lines[12].S_out)
# print(net.lines[12].Loss)










