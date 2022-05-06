import clases

persona = clases.Persona()

persona.setNombre ("Gerardo") 
persona.setApellidos("Olguin") 
persona.setEdad(40)
persona.setAltura(1.68)

print(f"la persona es : {persona.getNombre()} {persona.getApellidos()}") 

informatico = clases.Informatico()

informatico.setNombre("golguin")
informatico.setApellidos("olguin dom")

print(f"Informatico es : {informatico.getNombre()} {informatico.getApellidos()}") 
print(informatico.getLenguajes())