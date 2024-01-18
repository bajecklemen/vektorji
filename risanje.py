import matplotlib.pyplot as plt
 
class Risba():
    def __init__(self, v=3):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        #skrijemo osi
        self.ax.set_axis_off()
        #razpon
        self.ax.set_xlim([-v, v])
        self.ax.set_ylim([-v, v])
        self.ax.set_zlim([-v, v])
        #baza
    def baza(self):
        self.nič = (0,0,0)
        self.ax.quiver(self.nič[0],self.nič[1],self.nič[2], 2, 0, 0, color="r",normalize=True)
        self.ax.quiver(self.nič[0],self.nič[1],self.nič[2], 0, 2, 0, color="g",normalize=True)
        self.ax.quiver(self.nič[0],self.nič[1],self.nič[2], 0, 0, 2, color="b",normalize=True)
        self.ax.text(0.1, 0.0, -0.2, r'$0$')
        self.ax.text(0.5, 0, 0, r'$x$')
        self.ax.text(0, 0.5, 0, r'$y$')
        self.ax.text(0, 0, 0.5, r'$z$')
    def prikaži(self):
        plt.show()
    def vektor(self,v, ime='', barva = 'blue'):
        self.ax.quiver(0, 0, 0, v[0], v[1], v[2],color=barva)
        self.ax.text(v[0]/2, v[1]/2, v[2]/2, ime)
    def pvektor(self,z,v, ime='', barva = 'blue'):
        self.ax.quiver(z[0], z[1], z[2],v[0], v[1], v[2],color=barva)
        self.ax.text(z[0]+v[0]/2, z[1]+v[1]/2, z[0]+v[2]/2, ime)

if __name__ == "__main__":
    x = Risba(4)
    x.baza()
    a = (1,2,3)
    b = (-2,-1,3)
    n = (-1,1,6)
    x.vektor(a,'a','green')
    x.vektor(n,'n','black')
    x.pvektor(a,b,'b','blue')
    x.prikaži()
    





