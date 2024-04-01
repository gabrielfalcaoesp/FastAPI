from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

# Criação da conexão com o banco de dados
db_connection = mysql.connector.connect(
    host="senai114.mysql.database.azure.com",
    user="gabriel",
    password="senai114@",
    database="Loja"
)
db_cursor = db_connection.cursor()

# Definindo modelo de dados para inserção
class Item(BaseModel):
    name: str
    description: str = None

# Inicialização da aplicação FastAPI
app = FastAPI()

# Rota para exibir todos os itens
@app.get("/items/")
async def get_items():
    query = "SELECT * FROM items"
    db_cursor.execute(query)
    items = db_cursor.fetchall()
    return items


# Rota para retornar apenas 1 item
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    query = "SELECT * FROM items WHERE ID = %s"
    values = (item_id,)
    db_cursor.execute(query, values)
    items = db_cursor.fetchone()
    if items is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return items


# Rota para inserir dados
@app.post("/items/")
async def create_item(item: Item):
    query = "INSERT INTO items (name, description) VALUES (%s, %s)"
    values = (item.name, item.description)
    db_cursor.execute(query, values)
    db_connection.commit()
    return {"message": "Item inserido com sucesso"}

# Rota para deletar dados
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = "DELETE FROM items WHERE id = %s"
    values = (item_id,)
    db_cursor.execute(query, values)
    db_connection.commit()
    if db_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"message": "Item deletado com sucesso"}

# Executando a aplicação usando Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
