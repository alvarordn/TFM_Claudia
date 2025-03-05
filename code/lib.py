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

    def assign_x(self, x):
        index = 0
        for node in self.nodes:
            node.U = complex(x[index], x[index + 1])
            index += 2
            
    def compute_I(self):
        for line in self.lines:
            line.I = (line.nodes[0].U - line.nodes[1].U)/line.Z
        for node in self.nodes: # +: inyeccion, -: demanda
            node.I = np.conj(np.sum([complex(p.P, p.Q) for p in node.pros])/node.U)
    
    def compute_res(self):
        residual = []
        for node in self.nodes:
            residual.append(node.check())
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
        x0 = [1,0]*len(self.nodes)
        sol, infodict, ier, mesg = fsolve(self.test_x, x0, full_output = True)
        print(mesg)
        return sol, infodict, ier, mesg

class node:
    def __init__(self, ref, slack):
        self.ref = ref   
        self.slack = slack        
        self.lines = list()
        self.U = complex(1, 0)
        self.pros = []
    
    def check(self):
        if self.slack:
            residual = self.U - complex(1, 0)
        else:
            I_agregada = 0
            I_agregada += self.I
            for line in self.lines:
                if line.nodes[0] == self:
                    I_agregada -= line.I
                else:
                    I_agregada += line.I
            residual = I_agregada
        return residual
        
class line:
    def __init__(self, ref, From, To, Z_p, nodes_list):
        self.ref = ref 
        self.Z_p = Z_p # Sino guarod Z_p aquí es un argumento del constructor, pero no lo  guardo como atributo de la clase.
        self.G, self.B = np.real(1/self.Z_p), -np.imag(1/self.Z_p)
        self.Y = 1/self.Z_p
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
        
        
        
        
        
        
        
        
        
        
    