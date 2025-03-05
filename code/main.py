# Importing required libraries
import numpy as np
import lib
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
    


S_R1=200000 #VA
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


# Lines
Lines = [
    {'id': 0, 'From': 'X1', 'To': 'C2', 'Z_p': Z_pOH1 * L_a},
    {'id': 1, 'From': 'X1', 'To': 'C3', 'Z_p': Z_pOH1 * L_a},
    {'id': 2, 'From': 'X1', 'To': 'C4', 'Z_p': Z_pOH1 * L_a},
    {'id': 3, 'From': 'X1', 'To': 'C5', 'Z_p': Z_pOH1 * L_a},
    {'id': 4, 'From': 'X1', 'To': 'C6', 'Z_p': Z_pOH1 * L_a},
    {'id': 5, 'From': 'X1', 'To': 'C7', 'Z_p': Z_pOH1 * L_a},
    {'id': 6, 'From': 'X1', 'To': 'C8', 'Z_p': Z_pOH1 * L_a},
    {'id': 7, 'From': 'X1', 'To': 'C9', 'Z_p': Z_pOH1 * L_a},
    {'id': 8, 'From': 'X1', 'To': 'C10', 'Z_p': Z_pOH1 * L_a},
    {'id': 9, 'From': 'X1', 'To': 'C11', 'Z_p': Z_pOH1 * L_a},
    {'id': 10, 'From': 'X1', 'To': 'C12', 'Z_p': Z_pOH1 * L_a},
    {'id': 11, 'From': 'X1', 'To': 'C13', 'Z_p': Z_pOH1 * L_a},
    {'id': 12, 'From': 'X1', 'To': 'C14', 'Z_p': Z_pOH1 * L_a},
    {'id': 13, 'From': 'X1', 'To': 'C15', 'Z_p': Z_pOH1 * L_a},
    {'id': 14, 'From': 'X1', 'To': 'C16', 'Z_p': Z_pOH1 * L_a},
    {'id': 15, 'From': 'X1', 'To': 'C17', 'Z_p': Z_pOH1 * L_a},
    {'id': 16, 'From': 'X1', 'To': 'C18', 'Z_p': Z_pOH1 * L_a},
    {'id': 17, 'From': 'X1', 'To': 'C19', 'Z_p': Z_pOH1 * L_a},
    {'id': 18, 'From': 'X1', 'To': 'C20', 'Z_p': Z_pOH1 * L_a},
    {'id': 19, 'From': 'X1', 'To': 'C21', 'Z_p': Z_pOH1 * L_a},
    {'id': 20, 'From': 'X1', 'To': 'C22', 'Z_p': Z_pOH1 * L_a},
    {'id': 21, 'From': 'X1', 'To': 'C23', 'Z_p': Z_pOH1 * L_a},
    {'id': 22, 'From': 'X1', 'To': 'C24', 'Z_p': Z_pOH1 * L_a},
    {'id': 23, 'From': 'X1', 'To': 'C25', 'Z_p': Z_pOH1 * L_a},
    {'id': 24, 'From': 'X1', 'To': 'C26', 'Z_p': Z_pOH1 * L_a},
    {'id': 25, 'From': 'X1', 'To': 'C27', 'Z_p': Z_pOH1 * L_a},
    {'id': 26, 'From': 'X1', 'To': 'C28', 'Z_p': Z_pOH1 * L_a},
    {'id': 27, 'From': 'X1', 'To': 'C29', 'Z_p': Z_pOH1 * L_a},
    {'id': 28, 'From': 'X1', 'To': 'C30', 'Z_p': Z_pOH1 * L_a},
    {'id': 29, 'From': 'X1', 'To': 'C31', 'Z_p': Z_pOH1 * L_a},
    {'id': 30, 'From': 'X1', 'To': 'C32', 'Z_p': Z_pOH1 * L_a},
    {'id': 31, 'From': 'X1', 'To': 'C33', 'Z_p': Z_pOH1 * L_a},
    {'id': 32, 'From': 'X1', 'To': 'C34', 'Z_p': Z_pOH1 * L_a},
    {'id': 33, 'From': 'X1', 'To': 'C35', 'Z_p': Z_pOH1 * L_a},
    {'id': 34, 'From': 'X1', 'To': 'C36', 'Z_p': Z_pOH1 * L_a},
    {'id': 35, 'From': 'X1', 'To': 'C37', 'Z_p': Z_pOH1 * L_a},
    {'id': 36, 'From': 'X1', 'To': 'C38', 'Z_p': Z_pOH1 * L_a}
]

# Prosumers
Pros = [
    {'id': 0, 'Node': 'C2', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 1, 'Node': 'C3', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 2, 'Node': 'C4', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 3, 'Node': 'C5', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 4, 'Node': 'C6', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 5, 'Node': 'C7', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 6, 'Node': 'C8', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 7, 'Node': 'C9', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 8, 'Node': 'C10', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 9, 'Node': 'C11', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 10, 'Node': 'C12', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 11, 'Node': 'C13', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 12, 'Node': 'C14', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 13, 'Node': 'C15', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 14, 'Node': 'C16', 'P': -np.array([(S_R1*0.95)/3]*3), 'Q': -np.array([(S_R1*np.sin(np.arccos(0.95)))/3]*3)}
]


# Constructing network and solving power flow
net = lib.grid(Nodes, Lines, Pros)

sol, infodict, ier, mesg = net.solve_pf()

# Algunos comandos interesantes
# net.__dict__
# 
# net.nodes[0].lines[0].__dict__
# net.nodes[0].lines[0].nodes[0].__dict__

# for node in net.nodes:
#     print(node.__dict__)






