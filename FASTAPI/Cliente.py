from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Clinica" #Confirmar nome da database depois 
)
db_cursor = db_connection.cursor()


class Cliente(BaseModel):
    id_cliente: int
    nome: str
    data_de_nascimento: str 
    rg: str 
    cpf: str 
    email: str
    telefone: str 
    cep: str
    estado: str 
    cidade: str 
    bairro: str 
    endereco: str 
    numero: int 
    senha: str 
    genero: str 


app = FastAPI()


#Read de todos os valores -- Confirmar nome da tabela, se de fato é "Clientes" e confirmar se a rota também ficará como /Clientes 
@app.get("/Clientes/")
async def get_clientes():
    query = "SELECT * FROM Clientes"
    db_cursor.execute(query)
    clientes = db_cursor.fetchall()
    return clientes


#Read de 1 único os valor -- Confirmar nome da tabela, se de fato é "Clientes" e confirmar se a rota também ficará como /Clientes 
@app.get("/Clientes/{id_cliente}")
async def get_clientes(id_cliente: int):
    query = "SELECT * FROM Clientes WHERE ID = %s"
    values = (id_cliente)
    db_cursor.execute(query, values)
    clientes = db_cursor.fetchone()
    if clientes is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return clientes

#Create de Cliente -- Confirmar nome da tabela, se de fato é "Clientes" e confirmar se a rota também ficará como /Clientes 
@app.post("/Clientes/")
async def create_cliente(cliente: Cliente):
    query = "INSERT INTO Clientes (nome, data_de_nascimento, rg, cpf, email, telefone, cep, estado, cidade, bairro, endereco, numero, senha, genero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (cliente.nome, cliente.data_de_nascimento, cliente.rg, cliente.cpf, cliente.email, cliente.telefone, cliente.cep, cliente.estado, cliente.cidade, cliente.bairro, cliente.endereco, cliente.numero, cliente.senha, cliente.genero)
    db_cursor.execute(query, values)
    db_connection.commit()
    return {"message": "Item inserido com sucesso"}

#Fazer alteração 
@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item):
    query = "UPDATE items SET name = %s, description = %s WHERE ID = %s"
    values = (updated_item.name, updated_item.description, item_id)
    db_cursor.execute(query, values)
    # Verificar se algum registro foi atualizado
    if db_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    db_connection.commit()
    return {"message": "Item atualizado com sucesso"}
    

#Fazer alteração 
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = "DELETE FROM items WHERE id = %s"
    values = (item_id,)
    db_cursor.execute(query, values)
    db_connection.commit()
    if db_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"message": "Item deletado com sucesso"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
