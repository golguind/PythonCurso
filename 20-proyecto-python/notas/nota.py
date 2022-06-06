import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
    
    def guardar(self):

        sql = "Insert into notas values (null, %s, %s, %s, NOW())"
        nota = (self.usuario_id,self.titulo,self.descripcion)

        cursor.execute(sql, nota)
        database.commit()
        
        return(cursor.rowcount, self)