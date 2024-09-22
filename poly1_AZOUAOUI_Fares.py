#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Programme de AZOUAOUI Farès 

#Imports eventuels


#Declaration de classe et fonctions 

class Vecteur :
    def __init__(self,coeffs) :
        self.v = list(coeffs)
        print("Nouveau vecteur")
        
    def dimension(self) :
        return len(self.v)
    
    def get(self,i) :
        return self.v[i]
    
    def afficher(self) :
        print("[", end = ' ')
        for i in range(len(self.v)) :
            print (self.v[i],end = ' ')
            if i == len(self.v)-1 :
                print("]")
            else :
                print(";",end= ' ')
            
    def somme(self,vec2) : 
        if self.dimension() == vec2.dimension() :
            f = []
            for i in range (vec2.dimension()) :
                f.append(self.get(i) + vec2.get(i))
                return Vecteur(f)
        else :
            raise ValueError("Les 2 vecteurs ne sont pas de la même dimension")
                                

class Polynome(Vecteur):
    def __init__(self,coeffs) : 
        super().__init__(coeffs)
        self.coeffs = list(coeffs)
        print("Nouveau polynome")
        
    def degre(self) :
        return self.dimension()-1
    
    def afficher(self) : 
        print("P(x) =", end = ' ')
        for i in range(self.dimension()):
            print(self.get(i), "x^", i, end = '')
            if i != self.dimension() - 1 and self.get(i) >= 0 :
                print(" + ", end = '')
                print(end = ' ')
            else :
                print("\n")
                
    def somme(self, poly2):
        if self.dimension() == poly2.dimension():
            f = []
            for i in range(poly2.dimension()):
                f.append(self.get(i) + poly2.get(i))
            return self.__class__(f) 
        else: 
            raise ValueError("Les 2 polynomes ne sont pas de mêmes degrés")
    

    def evaluer(self, x):
        r = []
        q = 0
        for i in range(self.dimension()):
            r.append(self.get(i) * x**i)
        for i in range(len(r)) :
            q = q + r[i]
        return q
    
    def evaluer_horner(self, x):
        r = 0
        for coeff in reversed(self.coeffs):
            r = r * x + coeff
        return r
    
    
# Programme principal 

n = Vecteur([10,20])
m = Vecteur([5,-2,1.5])        
vr = Vecteur(range(4,8))
v = Vecteur([20,60])

print(n.dimension())
print(n.get(0))
m.afficher()
n.somme(v).afficher()


a = Polynome([25, 5])
a1 = Polynome([5, 25])
b = Polynome([10, 12,])
c = Polynome([2, 4, 6])
print(a.degre())
b.afficher()
b.somme(a1).afficher()
c.afficher()
print(c.evaluer(2))
print(c.evaluer_horner(2))
