#Un modulo es todos los archivos que termina en la extencion .py, sirve para crear un modulo donde por ejemplo carguemos funcionalidades y los llamamos en otro modulo principal, pero no siempre tenemos que hacer nuestros modulos por que muchas empresas crean modulos para que las gentes los usen

import MODULO_SALUDAR as m_saludar #VSC nos muestra todos los modulos con extencion .py que contiene
#Usando la propiedad "as" le podemos dar un nombre que queramos a el modulo y no tener que estar preocupandonos de escribirlo mal, que haya algun error

#saludo = m_saludar.Greeting("pepito")  #De esta forma estamos llamando a nuestra funcion (Greeting) que esta en otro modulo, pero aqui pasa a ser un metodo por eso creamos la lista (saludo) y le pasamos como metodo nuestra funcionalidad del modulo correspondiente.
#print(saludo)                               #En este caso le estamos pasando un PROP con un nombre y hacemos un print a la lista que creamos

#Si solo quiero importar la funcion del modulo se escribe de la siguiente forma, y es una buena practica a la hora de trabajar on modulos
from MODULO_SALUDAR import Greeting

saludo = Greeting("pepito")
print(saludo)


#Si yo quiero importar dos o mas funcionalidades se hace de la siguiente forma
from MODULO_SALUDAR import Greeting,Greeting_Bad

saludo = Greeting("pepito")
print(saludo)

saludo2 = Greeting_Bad("pepito")
print(saludo2)

#Para importar todo lo que contenga un modulo se escribe de la siguiente forma
from MODULO_SALUDAR import *

saludo = Greeting("pepito")
print(saludo)

saludo2 = Greeting_Bad("pepito")
print(saludo2)
