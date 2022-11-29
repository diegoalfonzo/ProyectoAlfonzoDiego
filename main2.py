from Persona import Persona
from Casa import Casa
from Hogar import Hogar

per = Persona("diego","19")

cas = Casa("406","Libertador")

print(per)
print(cas)


hog = Hogar(per,cas)

hog.mostrar()

per.nombre="Alfonso"
print("-----")
hog.mostrar()