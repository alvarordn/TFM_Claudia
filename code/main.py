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
S_R11= 15000
S_R15=52000
S_R16=55000
S_R17=35000
S_R18=47000

S_I2=100000

S_C1=120000
S_C12=20000
S_C13=20000
S_C14=25000
S_C17=25000
S_C18=8000
S_C19=16000
S_C20=8000

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
Pros = [
    {'id': 0,  'Node': 'R11', 'P': -np.array([(S_R11*0.95)/3]*3), 'Q': -np.array([(S_R11*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 1,  'Node': 'R15', 'P': -np.array([(S_R15*0.95)/3]*3), 'Q': -np.array([(S_R15*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 2,  'Node': 'R16', 'P': -np.array([(S_R16*0.95)/3]*3), 'Q': -np.array([(S_R16*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 3,  'Node': 'R17', 'P': -np.array([(S_R17*0.95)/3]*3), 'Q': -np.array([(S_R17*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 4,  'Node': 'R18', 'P': -np.array([(S_R18*0.95)/3]*3), 'Q': -np.array([(S_R18*np.sin(np.arccos(0.95)))/3]*3)},
    {'id': 5,  'Node': 'I2',  'P': -np.array([(S_I2*0.85)/3]*3),  'Q': -np.array([(S_I2*np.sin(np.arccos(0.85)))/3]*3)},
    {'id': 7,  'Node': 'C12', 'P': -np.array([(S_C12*0.90)/3]*3), 'Q': -np.array([(S_C12*np.sin(np.arccos(0.90)))/3]*3)},
    {'id': 8,  'Node': 'C13', 'P': -np.array([(S_C13*0.90)/3]*3), 'Q': -np.array([(S_C13*np.sin(np.arccos(0.90)))/3]*3)},
    {'id': 9,  'Node': 'C14', 'P': -np.array([(S_C14*0.90)/3]*3), 'Q': -np.array([(S_C14*np.sin(np.arccos(0.90)))/3]*3)},
    {'id': 10, 'Node': 'C17', 'P': -np.array([(S_C17*0.90)/3]*3), 'Q': -np.array([(S_C17*np.sin(np.arccos(0.90)))/3]*3)},
    {'id': 11, 'Node': 'C18', 'P': -np.array([(S_C18*0.90)/3]*3), 'Q': -np.array([(S_C18*np.sin(np.arccos(0.90)))/3]*3)},
    {'id': 12, 'Node': 'C19', 'P': -np.array([(S_C19*0.90)/3]*3), 'Q': -np.array([(S_C19*np.sin(np.arccos(0.90)))/3]*3)},
    {'id': 13, 'Node': 'C20', 'P': -np.array([(S_C20*0.90)/3]*3), 'Q': -np.array([(S_C20*np.sin(np.arccos(0.90)))/3]*3)}
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

print(net.pros[1].Iang)
print(net.pros[1].Imagn)
print(net.lines[12].Imag)
print(net.lines[12].Iang)
print(net.nodes[14].Uang)
print(net.nodes[14].Umag)
print(net.lines[12].S_in)
print(net.lines[12].S_out)
print(net.lines[12].Loss)




