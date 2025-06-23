# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 16:43:25 2025

@author: Usuario
"""

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
U_BAT = []
U_FC = []
U_DIESEL = []
U_HL = []
U_IL = []
U_PV = []
U_WT = []

for p in time[:3599]:
    # Prosumers
    Pros = []
    #VIVIENDAS PV
    for q in range(1,57): #no hay 0, va hasta el 56
        Pros.append([
            {'id': f"VIVIENDA.{q}",  'Node': q, 'P': np.array([(fdp_PV*PV[p])/3*0.005]*3), 'Q': np.array([(PV[p]*np.sin(np.arccos(fdp_PV)))/3*0.005]*3)}])
    #BLOQUES A PV
    for q in range(57,68): 
        Pros.append([
            {'id':  f"BLOQUE_A.{q}",  'Node': q, 'P': np.array([(fdp_PV*PV[p])/3*0.015]*3), 'Q': np.array([(PV[p]*np.sin(np.arccos(fdp_PV)))/3*0.015]*3)}])
    #BLOQUE B PV
    for q in range(68,78): 
        Pros.append([
            {'id':  f"BLOQUE_B.{q}",  'Node': q, 'P': np.array([(fdp_PV*PV[p])/3*0.03]*3), 'Q': np.array([(PV[p]*np.sin(np.arccos(fdp_PV)))/3*0.03]*3)}])
       # net = lib.grid(Nodes, Lines, Pros)
    #VIVIENDAS PV
    for q in range(78,81): #no hay 0, va hasta el 56
        Pros.append([
            {'id':  f"SUPER.{q}",  'Node': q, 'P': np.array([(fdp_PV*PV[p])/3*0.06]*3), 'Q': np.array([(PV[p]*np.sin(np.arccos(fdp_PV)))/3*0.06]*3)}])
        

    #sol, infodict, ier, mesg = net.solve_pf()

