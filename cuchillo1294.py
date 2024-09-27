class cuchillo:
    
    def diccionario_cliente_1294(self): 
        cliente = { 
        "Id_cliente.56965\n": "Nombre..luis miguel",
        "correo electronico..luis_miguel@gmail.com\n":"Telefono..656-458-1236",
        "direccion..C.Av de las torres\n":"Fecha de regisro.. 12 agosto de 2020",
        "preferencias.. hamburguesas": 7
        }
        print(cliente) 
        print("\n")
        for c, u in cliente.items():
            print(c,u)
        print("\n")
        
    def diccionario_empleado_1294(self): 
        Empleado = { 
        "Id_Empleado..56965\n": "Nombre..Jose Luis",
        "cargo.. cocinero\n":"Telefono..656-458-1236",
        "fecha de contratacion.. 16 de septiembe de 2024\n":"salario.. 1200 MX semanales",
        "experiencia laboral.. 15 dias": 7
        } 
        print(Empleado) 
        print("\n")
        for c, u in Empleado.items():
            print(c,u)
        print("\n")
        
    def diccionario_proveedores_1294(self): 
        proveedores = {
        "Id_proveedor..56965\n": "Nombre..Jose jose",
        "contacto.. 656-458-1251\n":"Telefono.. 229-125-1203",
        "correo electronico.. jose@gmail.com\n":"Direccion..C.plutarco elias calles",
        "Tipo de producto.. pan": 7
        } 
        print(proveedores) 
        print("\n")
        for c, u in proveedores.items():
            print(c,u)
        print("\n")
        
    def diccionario_Tienda_1294(self): 
        tienda = { 
        "Id_Empleado..56965\n": "Nombre..cuchillo",
        "Direccion.. Av. de las torres\n":"Telefono..656-458-1236",
        "correo electronico.. cuchillo@gmail.com\n":"horario.. 9am - 11pm",
        "tipó de producto.. hamburguesa, papas fritas": 7
        } 
        print(tienda) 
        print("\n")
        for c, u in tienda.items():
            print(c,u)
        print("\n")
        

x = cuchillo ()
x.diccionario_cliente_1294()
x.diccionario_empleado_1294()
x.diccionario_proveedores_1294()
x.diccionario_Tienda_1294

