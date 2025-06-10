# Importing required libraries
import numpy as np
import lib
import scipy.io
#en desiquilibrado no trabajamos en por unidad
#Sbase = 1e6
Ubase = 400 #V
#Zbase = (Ubase**2)/Sbase

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
    

S_base = 100000 
fdp_bat = 1
fdp_PV = 1
fdp_WT = 0.99
fdp_IL = 0.95
fdp_HL = 1
fdp_DIESEL = 0.95
fdp_FC= 0.97
#PERFILES EN PU
# Cargar el archivo
mat = scipy.io.loadmat('Profile_3600_pu.mat')

# Extraer la estructura
profile = mat['Profile_3600_pu']

# Acceder a los campos (por ejemplo, el campo BAT)
bat = profile['BAT'][0][0].flatten()*S_base  # 3600 valores
PV = profile['PV'][0][0].flatten()*S_base
FC= profile['CHPFC'][0][0].flatten()*S_base
DIESEL = profile['CHPDIESEL'][0][0].flatten()*S_base
IL = profile['IL'][0][0].flatten()*S_base
HL = profile['HL'][0][0].flatten()*S_base
WT= profile['WT'][0][0].flatten()*S_base
time= profile['time'][0][0].flatten()
# Nodes
Nodes = [
    {'id': 'X1', 'slack': True},
    {'id': 'BAT', 'slack': False},
    {'id': 'FC', 'slack': False},
    {'id': 'DIESEL', 'slack': False},
    {'id': 'IL', 'slack': False},
    {'id': 'HL', 'slack': False},
    {'id': 'PV', 'slack': False},
    {'id': 'WT', 'slack': False},
]


# Lines
Lines = [
    {'id': 0, 'From': 'X1', 'To': 'BAT', 'Z_p': Z_pUG1 * L_a},
    {'id': 1, 'From': 'X1', 'To': 'FC', 'Z_p': Z_pUG1 * L_a},
    {'id': 2, 'From': 'X1', 'To': 'DIESEL', 'Z_p': Z_pUG1 * L_a},
    {'id': 3, 'From': 'X1', 'To': 'IL', 'Z_p': Z_pUG1 * L_a},
    {'id': 4, 'From': 'X1', 'To': 'HL', 'Z_p': Z_pUG1 * L_a},
    {'id': 5, 'From': 'X1', 'To': 'PV', 'Z_p': Z_pUG1 * L_a},
    {'id': 6, 'From': 'X1', 'To': 'WT', 'Z_p': Z_pUG1 * L_a}]


P_head = []
U_range = []
for p in time[:3599]:
    # Prosumers
    Pros = [
        {'id': 1,  'Node': 'BAT', 'P': np.array([(fdp_bat*bat[p])/3]*3), 'Q': np.array([(bat[p]*np.sin(np.arccos(fdp_bat)))/3]*3)},
        {'id': 2,  'Node': 'FC', 'P': np.array([(fdp_FC*FC[p])/3]*3), 'Q': np.array([(FC[p]*np.sin(np.arccos(fdp_FC)))/3]*3)}, 
        {'id': 3,  'Node': 'DIESEL', 'P': np.array([(fdp_DIESEL*DIESEL[p])/3]*3), 'Q': np.array([(DIESEL[p]*np.sin(np.arccos(fdp_DIESEL)))/3]*3)},
        {'id': 4,  'Node': 'IL', 'P': -np.array([(fdp_IL*IL[p])/3]*3), 'Q': -np.array([(IL[p]*np.sin(np.arccos(fdp_IL)))/3]*3)}, 
        {'id': 5,  'Node': 'HL', 'P': -np.array([(fdp_HL*HL[p])/3]*3), 'Q': -np.array([(HL[p]*np.sin(np.arccos(fdp_HL)))/3]*3)}, 
        {'id': 6,  'Node': 'PV', 'P': np.array([(fdp_PV*PV[p])/3]*3), 'Q': -np.array([(PV[p]*np.sin(np.arccos(fdp_PV)))/3]*3)}, 
        {'id': 7,  'Node': 'WT', 'P': -np.array([(fdp_WT*WT[p])/3]*3), 'Q': -np.array([(WT[p]*np.sin(np.arccos(fdp_WT)))/3]*3)}]

    net = lib.grid(Nodes, Lines, Pros)


    #sol, infodict, ier, mesg = net.solve_pf()

    sol, _, _, _ = net.solve_pf()  # Ignora infodict, ier y mesg


    S_temp = net.nodes[0].U[0]*np.conj(net.nodes[0].I[0])+net.nodes[1].U[1]*np.conj(net.nodes[1].I[1])+net.nodes[2].U[2]*np.conj(net.nodes[2].I[0])
    
    P_head.append(S_temp.real)
    
    U_fases = net.nodes[0].U[:3] 
    U_range.append(abs(np.mean(np.abs(U_fases))))

print(P_head)
        

# Constructing network and solving power flow

# Algunos comandos interesantes
# net.__dict__
# 
# net.nodes[0].lines[0].__dict__
# net.nodes[0].lines[0].nodes[0].__dict__

# for node in net.nodes:
#     print(node.__dict__)

#para graficar la potencia
# import matplotlib.pyplot as plt

# plt.plot(time, P_range)
# plt.title("Potencia de cabecera")
# plt.xlabel("Tiempo")
# plt.ylabel("Potencia")  # Etiqueta genérica sin unidades
# plt.grid(True)
# plt.tight_layout()
# plt.show()



