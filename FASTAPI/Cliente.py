from fastapi import FastAPI, HTTPException, Form
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
async def create_cliente(
    nome: str = Form(...),
    data_de_nascimento: str = Form(...),
    rg: str = Form(...),
    cpf: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cep: str = Form(...),
    estado: str = Form(...),
    cidade: str = Form(...),
    bairro: str = Form(...),
    endereco: str = Form(...),
    numero: str = Form(...),
    senha: str = Form(...),
    genero: str = Form(...)
):
    query = "INSERT INTO Clientes (nome, data_de_nascimento, rg, cpf, email, telefone, cep, estado, cidade, bairro, endereco, numero, senha, genero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nome, data_de_nascimento, rg, cpf, email, telefone, cep, estado, cidade, bairro, endereco, numero, senha, genero)
    db_cursor.execute(query, values)
    db_connection.commit()
    return {"message": "Cliente inserido com sucesso"}

#Fazer alteração 
@app.put("/Clientes/{cliente_id}")
async def update_cliente(cliente_id: int, updated_cliente: Cliente):
    query = "UPDATE Clientes SET nome = %s, data_de_nascimento = %s, rg = %s, cpf = %s, email = %s, telefone = %s, cep = %s, estado = %s, cidade = %s, bairro = %s, endereco = %s, numero = %s, senha = %s, genero = %s WHERE ID = %s"
    values = (updated_cliente.nome, updated_cliente.data_de_nascimento, updated_cliente.rg, updated_cliente.cpf, updated_cliente.email, updated_cliente.telefone, updated_cliente.cep, updated_cliente.estado, updated_cliente.cidade, updated_cliente.bairro, updated_cliente.endereco, updated_cliente.numero, updated_cliente.senha, updated_cliente.genero, cliente_id)
    db_cursor.execute(query, values)
    # Verificar se algum registro foi atualizado
    if db_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db_connection.commit()
    return {"message": "Item atualizado com sucesso"}
    

#Fazer alteração 
@app.delete("/Clientes/{cliente_id}")
async def delete_cliente(cliente_id: int):
    query = "DELETE FROM Clientes WHERE id = %s"
    values = (cliente_id,)
    db_cursor.execute(query, values)
    db_connection.commit()
    if db_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"message": "Cliente deletado com sucesso"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.2", port=8000)
