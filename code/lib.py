# Importing required libraries
import numpy as np
from scipy.optimize import fsolve



class grid:
    def __init__(self, nodes, lines, pros):
        self.nodes = self.add_nodes(nodes)                                      
        self.lines = self.add_lines(lines, self.nodes)  
        self.pros = self.add_pros(pros, self.nodes)  
                
    def add_nodes(self, nodes):
        nodes_list = list()
        for item in nodes:
            nodes_list.append(node(item['id'], item['slack']))
        return nodes_list
        
    def add_lines(self, lines, nodes):
        lines_list = list()
        for item in lines:
            lines_list.append(line(item['id'], item['From'], item['To'], item['Z_p'], nodes))
        return lines_list
        
    def add_pros(self, pros, nodes):
        pros_list = list()
        for item in pros:
            pros_list.append(prosumer(item['id'], item['Node'], item['P'], item['Q'], nodes))
        return pros_list

    # vector tensión slack y vector vacío de tensiones
    def assign_x(self, x):
        index = 0
        r = 400/np.sqrt(3)
        for node in self.nodes:
            if node.slack == True:
                node.U = np.array([complex(r*np.cos(0), r*np.sin(0)),
                                   complex(r*np.cos(-np.pi*120/180), r*np.sin(-np.pi*120/180)),
                                   complex(r*np.cos(np.pi*120/180), r*np.sin(np.pi*120/180)), 
                                   0])
            else: 
                node.U = np.array([complex(x[index + 0], x[index + 1]),
                                   complex(x[index + 2], x[index + 3]),
                                   complex(x[index + 4], x[index + 5]),
                                   complex(x[index + 6], x[index + 7])])
                index += 8
            

    
    

 
    # cambiado I linea, pendiente cambiar I inyectada 
    def compute_I(self):
        for line in self.lines:
            line.I = line.Y.dot(line.nodes[0].U - line.nodes[1].U)
        for node in self.nodes: # +: inyeccion, -: demanda
            S_node = np.array([0,0,0], dtype=complex)
            for p in node.pros:
                S_node += np.array([complex(item[0], item[1]) for item in zip(p.P, p.Q)])
            for index in range(3):
                node.I[index] = np.conjugate((S_node[index])/(node.U[index] - node.U[3]))
            node.I[3] = -np.sum(node.I[:3])
            
            
    
    def compute_res(self):
        residual = []
        for node in self.nodes[1:]:
            residual += node.check()
        residual_rx = []
        for item in residual:
            residual_rx.append(np.real(item))
            residual_rx.append(np.imag(item))
        return residual_rx
    
    def test_x(self, x):
        self.assign_x(x)
        self.compute_I()
        res = self.compute_res()
        return res
        
    def solve_pf(self):
        r = 400/np.sqrt(3)
        U0 = [r*np.cos(0), 
              r*np.sin(0),
              r*np.cos(-np.pi*120/180), 
              r*np.sin(-np.pi*120/180),
              r*np.cos(np.pi*120/180), 
              r*np.sin(np.pi*120/180), 
              0,
              0]        
        x0 = U0*(len(self.nodes) - 1)
        sol, infodict, ier, mesg = fsolve(self.test_x, x0, full_output = True)
        print(mesg)
        # LLAMADA A NUEVO MÉTODO
        self.compute_magnitudes()
       
    #     Umag = self.compute_magnitudes()
    #     for i, mags in enumerate(Umag):
    #         print(f"Módulos de tensión nodo {self.nodes[i].ref}:", mags)
        return sol, infodict, ier, mesg
    
    def compute_magnitudes(self):
        for node in self.nodes:
            magnitudes_node = []
            angles_node = []
            
            for p in node.U:
                magnitudes_node.append(abs(p)) 
                angles_node.append(np.angle(p, deg=True)) 
            node.Umag = magnitudes_node
            node.Uang = angles_node
        # CÁLCULO DE MÁGNITUDES DE PROSUMER: INTENSIDAD
        for prosumer in self.pros:
            magnitudes_pros = []
            angles_pros = []
            for i in range(3):
                I_mag = ((prosumer.P[i] - prosumer.Q[i]*1j)/np.conjugate(prosumer.node.U[i]))
                magnitudes_pros.append(abs(I_mag)) 
                angles_pros.append(np.angle(I_mag, deg=True)) 
            prosumer.Imagn = magnitudes_pros
            prosumer.Iang = angles_pros
        # debería de atrubuirse a pros net.pros[0].Imagn
        # CÁLCULO DE MÁGNITUDES DE LÍNEA: INTENSIDAD DE LÍNEA, flujos de potencia
        for line in self.lines:
            magnitudes_line_I = []
            angles_line_I = []
            magnitudes_in = []
            magnitudes_out =[]
            magnitudes_loss = []
            
            for i in range(3):
                S_in = line.nodes[0].U[i]*np.conjugate(line.I[i])
                S_out = line.nodes[1].U[i]*np.conjugate(line.I[i])
                Loss = S_in - S_out
                magnitudes_in.append(S_in)
                magnitudes_out.append(S_out)
                magnitudes_loss.append(Loss)
            for p in line.I:
                magnitudes_line_I.append(abs(p)) 
                angles_line_I.append(np.angle(p, deg=True)) 
            
            line.Imag = magnitudes_line_I
            line.Iang = angles_line_I
            line.S_in = magnitudes_in
            line.S_out = magnitudes_out
            line.Loss =  magnitudes_loss
            
        #CÁLCULO DE LAS PÉRDIDAS TOTALES
        self.total_losses = np.sum(np.array(line.Loss) for line in self.lines)
            
                
       

class node:
    def __init__(self, ref, slack):
        self.ref = ref   
        self.slack = slack        
        self.lines = list()
        self.U = None
        self.I = np.array([0, 0, 0, 0], dtype=complex)
        self.pros = []
    
    def check(self):
        if self.slack:
            return None
        else:
            I_agregada = np.array([0, 0, 0, 0], dtype=complex)
            I_agregada += self.I
            for line in self.lines:
                if line.nodes[0] == self:
                    I_agregada -= line.I
                else:
                    I_agregada += line.I
            I_agregada
        return list(I_agregada)
        
class line:
    def __init__(self, ref, From, To, Z_p, nodes_list):
        self.ref = ref 
        self.Z = Z_p # Sino guarod Z_p aquí es un argumento del constructor, pero no lo  guardo como atributo de la clase.
        self.Y = np.linalg.inv(Z_p)
        self.G, self.B = np.real(self.Y), -np.imag(self.Y)
        self.nodes = [next((item for item in nodes_list if item.ref == From), None), 
                      next((item for item in nodes_list if item.ref == To), None)]   
        self.nodes[0].lines.append(self)
        self.nodes[1].lines.append(self)
        
    
            
  
class prosumer:
    def __init__(self, ref, node_id, P, Q, nodes_list):
        self.ref = ref
        self.P = P
        self.Q = Q  
        self.node = next((item for item in nodes_list if item.ref == node_id), None)
        self.node.pros.append(self)
    
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
    