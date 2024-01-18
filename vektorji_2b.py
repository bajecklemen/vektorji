import math

def nasprotni(x):
    return (-x[0],-x[1], -x[2])
def vsota(x,y):
    return (x[0]+y[0],x[1]+y[1],x[2]+y[2])
def razlika(x,y):
    return vsota(a,nasprotni(b))
def skalarni(x,y):
    return x[0]*y[0]+x[1]*y[1]+x[2]*y[2]
def dolzina(x,y):
    return math.sqrt(skalarni(x,y))
def vkrats(x,s):
    return (x[0]*s,x[1]*s,x[2]*s)

a = (1,1,1)
b = (2,1,0)
print(vkrats(a,5))
    
