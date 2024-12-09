# Use uma imagem base com Python
FROM python:3.9-slim

# Crie um diretório para a aplicação
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta onde o Flask será executado
EXPOSE 4000

# Defina as variáveis de ambiente necessárias
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Comando para rodar a aplicação com gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:4000", "run:app"]
