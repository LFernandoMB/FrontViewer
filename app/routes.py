from flask import render_template
import sqlite3
from . import app
import requests # type: ignore
import base64
import json


# Função para buscar dados das tabelas
def fetch_data(db_name, query):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    # Consultas SQL para extrair dados das tabelas
    # db_path_mock = r"C:\Users\luis.bezerra\PycharmProjects\DemoAuth\assets\mock.db"
    db_path_offline = r"C:\Users\luis.bezerra\PycharmProjects\DemoAuth\assets\offline_data.db"
    
    banco_local = fetch_data(db_path_offline, "SELECT * FROM pending_data")
    registro_unico = fetch_data(db_path_offline, "SELECT * FROM daily_log")
    
    # dados_recebidos = fetch_data(db_path_mock, "SELECT * FROM get_data")
    # dados_enviados = fetch_data(db_path_mock, "SELECT * FROM set_data")
    
    data_request = requests.get("http://localhost:3000/get_data/6188")
    
    dados_recebidos = []
    for row in data_request.json():
        vetor_bytes = row['vetor'].encode('utf-8') # Convert string to bytes for decoding
        decoded_vetor = base64.b64decode(vetor_bytes).decode('utf-8') # Decode base64 and convert back to string
        
        row['vetor'] = json.loads(decoded_vetor)  # Update vetor with decoded and converted (str to list) value
        dados_recebidos.append(list(row.values()))    
    
    dados_enviados = requests.get("http://localhost:3000/set_data")
    
    # print(f"Local: {banco_local}")
    # print(f"Único: {registro_unico}")
    # print(f"Recebidos: {dados_recebidos}")
    # print(f"Enviados: {dados_enviados.json()}")

    # Renderiza o template HTML com os dados
    return render_template(
        'index.html',
        banco_local=banco_local,
        registro_unico=registro_unico,
        dados_recebidos=dados_recebidos,
        dados_enviados=dados_enviados.json()
    )
